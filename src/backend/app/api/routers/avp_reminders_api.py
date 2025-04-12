"""
All operations regarding reminders for AVP (izpit iz CPP & voznje). Retrieving reminders, creating one, deleting one, editing...
"""
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status, Query, HTTPException, Form
from sqlalchemy import select

# Auth

# Dependency
from app.api.dependencies.core import DBSessionDep
# from app.crud.vehicle_operations import get_vehicle_from_db, get_filter_page_from_db

# Shared
from shared.config import settings
from shared.db.models import Reminder
from shared.schemas.base import SuccessMsg, WarningMsg, BaseMsg
from shared.schemas.avp import ReminderSchema


router = APIRouter(
    prefix="/api/avp",
    tags=["avp", "termini"],
    # dependencies=[Depends(is_request_coming_from_gateway)],
    responses={404: {"description": "Not found"}},
)


# GET /reminders for email
@router.get(
    "/reminders",
)
async def list_reminders(email: str, db_session: DBSessionDep) -> list[dict, ]:
    reminders = await db_session.execute(
        select(Reminder).where(Reminder.email == email)
    )

    reminders = reminders.scalars().all()
    
    return [r.as_dict() for r in reminders]


# POST / PUT / DELETE /reminder
@router.post(
    "/reminder",
)
async def create_reminder(
    reminder: ReminderSchema, db_session: DBSessionDep
) -> BaseMsg:
    reminder_db = Reminder()
    for key, val in reminder.model_dump().items():
        reminder_db.__setattr__(key, val)

    db_session.add(reminder_db)
    # db_session.commit()

    return SuccessMsg(description="Reminder created.", data={
        "reminder_id": reminder_db.reminder_id
    })


@router.put(
    "/reminder/{reminder_id}",
)
async def edit_reminder(
    reminder_id: int, reminder: ReminderSchema, db_session: DBSessionDep
) -> BaseMsg:
    reminder_db = await db_session.get(Reminder, reminder_id)

    if reminder_db:
        for key, val in reminder.model_dump().items():
            reminder_db.__setattr__(key, val)
        # db_session.commit()

        return SuccessMsg(description="Reminder modified.")
    else:
        return WarningMsg(description="Reminder does not exist.")


@router.delete(
    "/reminder/{reminder_id}",
)
async def delete_reminders(
    reminder_id: int, db_session: DBSessionDep
) -> BaseMsg:
    reminder_db = await db_session.get(Reminder, reminder_id)

    if reminder_db:
        db_session.delete(reminder_db)
        # db_session.commit()
        return SuccessMsg(description="Reminder deleted.")
    else:
        return WarningMsg(description="Reminder does not exist.")
