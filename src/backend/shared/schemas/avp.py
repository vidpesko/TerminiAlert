from typing import Literal, Annotated, List
from datetime import datetime

from pydantic import BaseModel, AfterValidator, EmailStr, Field


class Filters(BaseModel):
    exam_type: Literal["VSE", 1, 2, "1", "2"] = "VSE"
    cat: List[Literal["VSE", 1, "1", 2, "2", 3, "3", 4, "4", 5, "5", 6, "6", 7, "7", 8, "8", 9, "9", 10, "10", 11, "11", 12, "12", 13, "13", 14, "14", 15, "15", 16, "16", 17, "17"]] = ["VSE", ]
    location_district: Literal[-1, "-1", 17, "17", 18, "18", 19, "19", 20, "20", 21, "21"] = -1
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


# class ReminderUpdate()
