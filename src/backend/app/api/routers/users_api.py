"""
All operations regarding user creation, account edit, deletion, authentication,...
"""
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status, Query, HTTPException
from sqlalchemy import select

# Auth

# Dependency
from app.api.dependencies.core import DBSessionDep

# from app.crud.vehicle_operations import get_vehicle_from_db, get_filter_page_from_db

# Shared
from shared.config import settings
from shared.db.models import Reminder


router = APIRouter(
    prefix="/user",
    tags=["users"],
    # dependencies=[Depends(is_request_coming_from_gateway)],
    responses={404: {"description": "Not found"}},
)
