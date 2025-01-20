from typing import Any

from pydantic import BaseModel


class SuccessResponse(BaseModel):
    status: str = "success"
    details: Any


class ErrorResponse(BaseModel):
    status: str = "error"
    details: Any
