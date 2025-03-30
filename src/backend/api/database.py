import json
import contextlib
from typing import Any, AsyncIterator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.collections import InstrumentedList

from shared.config import settings


class Base(DeclarativeBase):
    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#preventing-implicit-io-when-using-asyncsession
    __mapper_args__ = {"eager_defaults": True}

    relationships = []
    focus_on = None
    name_table = {}

    def as_dict(self, go_deep=False, remove_fk=False) -> dict:
        """Convert sqlalchemy class into dict while recursively exploring object relationships

        Object attributes to control this:
            - relationships (tuple{index, attr name}): required if you set go_deep to True. All specified relationships will be expanded and inserted into output dict at the specifed index
            - focus_on: set this to attribute name. It will return only that attribute
            - name_table (dict{old attr name, ne attr name}): use this attribute to rename attribute keys in output dict

        Args:
            go_deep (bool, optional): If you wish to explore object relationships. Defaults to False.
            TODO remove_fk (bool, optional): _description_. Defaults to False.

        Returns:
            dict: dict representation of object
        """

        obj_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        if self.focus_on:
            attr = getattr(self, self.focus_on)
            if isinstance(attr, Base):
                attr = attr.as_dict(go_deep=go_deep, remove_fk=remove_fk)
            return attr

        if remove_fk:
            for col in self.__table__.columns:
                if col.foreign_keys != set():
                    del obj_dict[col.name]
        if go_deep:
            for pos, col_name in self.relationships:
                value = getattr(self, col_name)
                if isinstance(value, list):
                    value = [v.as_dict(go_deep=True) for v in value]
                else:
                    value = value.as_dict(go_deep=True)

                keys = list(obj_dict.keys())
                keys.insert(pos, col_name)
                obj_dict = {k: obj_dict.get(k, value) for k in keys}

        if self.name_table:
            obj_dict = {
                self.name_table.get(old_key, old_key): val
                for old_key, val in obj_dict.items()
            }

        return obj_dict


# Heavily inspired by https://praciano.com.br/fastapi-and-async-sqlalchemy-20-with-pytest-done-right.html
class DatabaseSessionManager:
    def __init__(self, async_host: str, engine_kwargs: dict[str, Any] = {}):
        self._async_engine = create_async_engine(async_host, **engine_kwargs)
        # self._sync_engine = create_engine(sync_host, **engine_kwargs)  # sync engine is used only for db migration

        self._sessionmaker = async_sessionmaker(
            autocommit=False, bind=self._async_engine, expire_on_commit=False
        )

    async def close(self):
        if self._async_engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._async_engine.dispose()

        self._async_engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._async_engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._async_engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def create_tables(self):
        async with self._async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


session_manager = DatabaseSessionManager(
    settings.create_engine_url(async_driver=True),
    {"echo": settings.echo_sql},
)


async def get_db_session():
    async with session_manager.session() as session:
        yield session
