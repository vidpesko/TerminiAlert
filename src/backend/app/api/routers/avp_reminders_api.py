"""
All operations regarding reminders for AVP (izpit iz CPP & voznje). Retrieving reminders, creating one, deleting one, editing...
"""
from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Depends, Response, status, Query, HTTPException
from sqlalchemy import select
from sqlalchemy.orm.attributes import flag_modified

# Auth

# Dependency
from app.api.dependencies.core import DBSessionDep
# from app.crud.vehicle_operations import get_vehicle_from_db, get_filter_page_from_db

# Shared
from shared.config import settings
from shared.db.models import Reminder, ReminderUpdate
from shared.schemas.base import SuccessMsg, WarningMsg, BaseMsg
from shared.schemas.avp import ReminderSchema, SetSlotSchema


router = APIRouter(
    prefix="/avp",
    tags=["avp", "termini"],
    # dependencies=[Depends(is_request_coming_from_gateway)],
    responses={404: {"description": "Not found"}},
)


# GET /updates for email
@router.get(
    "/updates",
)
async def list_reminders(email: str, db_session: DBSessionDep) -> list[dict,]:
    reminders = await db_session.execute(
        select(Reminder).where(Reminder.email == email)
    )

    updates = []
    reminders = reminders.scalars().all()
    print(reminders[0].updates)
    return []

    for reminder in reminders:
        updates += reminder.updates

    return [u.as_dict() for u in updates]


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

    reminder_db.current_date = reminder_db.current_date.replace(tzinfo=None)

    db_session.add(reminder_db)

    await db_session.commit()

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
        await db_session.commit()

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
        await db_session.delete(reminder_db)
        await db_session.commit()
        return SuccessMsg(description="Reminder deleted.")
    else:
        return WarningMsg(description="Reminder does not exist.")


# POST /set-slot: set found_date as suggested_date or reject it
@router.post(
    "/set-slot",
)
async def set_slot(
    slot: SetSlotSchema,
    db_session: DBSessionDep,
) -> BaseMsg:
    reminder_db = await db_session.get(Reminder, slot.reminder_id)

    if not reminder_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reminder does not exist.",
        )

    if not reminder_db.found_dates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There are no found dates to confirm.",
        )

    found_date = None
    for fd in reminder_db.found_dates:
        if fd["id"] == slot.slot_id:
            found_date = fd
            break

    if not found_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There is no found date with the given slot_id.",
        )

    date = datetime.strptime(found_date["date"], "%Y-%m-%d %H:%M:%S")

    # Set suggested date
    if slot.action == "accept":
        reminder_db.suggested_date = date
    elif reminder_db.suggested_date == date:
        reminder_db.suggested_date = None
    # Update found date status
    for i, fd in enumerate(reminder_db.found_dates):
        if fd["id"] == slot.slot_id:
            reminder_db.found_dates[i]["status"] = slot.action + "ed"
            break

    flag_modified(reminder_db, "found_dates")

    await db_session.commit()

    return SuccessMsg(description=f"Slot {slot.action}ed.")
