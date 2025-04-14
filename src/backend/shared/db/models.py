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
    current_date: Mapped[DateTime] = mapped_column(DateTime)
    suggested_date: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    excluded_dates: Mapped[Optional[dict]] = mapped_column(JSONB)  # Format: [date 1, date 2,...]

    frequency: Mapped[Optional[str]] = mapped_column(default="medium")
    service_name: Mapped[str]
    filters: Mapped[Optional[dict]] = mapped_column(JSONB)
    service_url: Mapped[Optional[str]]

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    updates: Mapped[List["ReminderUpdate"]] = relationship(back_populates="reminder")

    def __str__(self):
        return f"Reminder(email={self.email}, service={self.service_name})"


class AvpSlot(Base):
    __tablename__ = "avp_slots"

    slot_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    service_name: Mapped[str] = mapped_column(nullable=False)

    date: Mapped[DateTime] = mapped_column(DateTime)
    spots_left: Mapped[int]
    exam_type: Mapped[str]
    categories: Mapped[dict] = mapped_column(JSONB)  # Format: [cat 1, cat 2,...]
    duration: Mapped[int]
    location_district: Mapped[str]
    location: Mapped[str]

    service_url: Mapped[str]
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __str__(self):
        return f"Slot(service={self.service_name}, date={self.date})"


class ReminderUpdate(Base):
    __tablename__ = "reminder_updates"

    update_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    reminder_id: Mapped[Optional[int]] = mapped_column(ForeignKey("reminders.reminder_id"), nullable=True)

    current_date: Mapped[DateTime] = mapped_column(DateTime)
    new_date: Mapped[DateTime] = mapped_column(DateTime)

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    reminder: Mapped[Reminder] = relationship(back_populates="updates", lazy="joined")

    def __str__(self):
        return f"ReminderUpdate(old date={self.current_date}, new date={self.new_date})"
