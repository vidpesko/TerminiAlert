from sys import path
from pathlib import Path

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from shared.config import settings
    from shared.db.models import Reminder
except ModuleNotFoundError:
    path.append(str(Path.cwd().parent))
    from shared.config import settings
    from shared.db.models import Reminder

try:
    from app.database import session_manager
    from app.api.routers import avp_reminders_api, users_api
except ModuleNotFoundError:
    path.append(str(Path.cwd()))
    from app.database import session_manager
    from app.api.routers import avp_reminders_api, users_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Execute on startup
    # Reflected.prepare(session_manager._sync_engine)  # Reflect db using sync engine
    # session_manager._sync_engine.dispose()  # Close that engine, it won't be needed
    await session_manager.create_tables()

    yield

    # Execute on exit
    if session_manager._async_engine is not None:
        # Close the DB connection
        await session_manager.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.project_name,
    summary="",
    description="",
)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:5173"],  # Svelte dev server
    allow_origins=[
        "https://termini.pesko.si",
        "https://termini.pesko.si",
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# Users router: all user operations
app.include_router(users_api.router, include_in_schema=False)

# AVP router: all operations regarding AVP services
app.include_router(avp_reminders_api.router)


if __name__ == "__main__":
    uvicorn.run(app, port=8008, host="0.0.0.0")
