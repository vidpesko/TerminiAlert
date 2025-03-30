from typing import Optional, List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy import BigInteger, String, Text, func, Table, DateTime, ForeignKey

from . import Base


class Reminder(Base):
    __tablename__ = "reminders"

    reminder_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    reminder_name: Mapped[Optional[str]] = mapped_column(default="Opomnik")

    frequency: Mapped[Optional[str]] = mapped_column(default="medium")
    service_name: Mapped[str]
    filters: Mapped[Optional[dict]] = mapped_column(JSONB)

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __str__(self):
        return f"Reminder(email={self.email}, service={self.service_name})"
