from pydantic import BaseModel


class BaseMsg(BaseModel):
    status: str = "Success"
    description: str | None = None
    data: dict = {}


class SuccessMsg(BaseMsg):
    status: str = "Success"


class WarningMsg(BaseMsg):
    status: str = "Warning"
