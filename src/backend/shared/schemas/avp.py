from typing import Literal, Annotated
from datetime import datetime

from pydantic import BaseModel, AfterValidator, EmailStr, Field


class Filters(BaseModel):
    exam_type: Literal["VSE", 1, 2] = "VSE"
    cat: Literal["VSE", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] = "VSE"
    location_district: Literal[-1, 17, 18, 19, 20, 21] = -1
    location: int = -1
    calendar_date: datetime | None = None


class ReminderSchema(BaseModel):
    email: EmailStr
    reminder_name: str | None = None
    current_date: datetime
    excluded_dates: list[datetime, ] | None = None

    frequency: Literal["low", "mid", "high"]
    service_name: str = "avp"
    filters: Filters
