from sys import path
from pathlib import Path

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from shared.config import settings
from api.database import session_manager
# from api.routers import car, reminders
from shared.db.models import Reminder


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
    allow_origins=["http://localhost:5173"],  # Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Vehicle router: all operations regarding scraping & retriving vehicles
# app.include_router(car.router)
# Reminders router: all operations for app "Avtonet Obvescanje"
# app.include_router(reminders.router, include_in_schema=False)


if __name__ == "__main__":
    uvicorn.run(app, port=80, host="0.0.0.0")
