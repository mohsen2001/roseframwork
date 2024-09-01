from pydantic_core.core_schema import ModelSchema
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class RoseSchema(ModelSchema):
    user_created: int
    ip_created: str
    date_created: datetime
    record_uuid: UUID
    ip_updated: Optional[str] = None
    user_updated: Optional[int] = None
    date_updated: datetime

    class Config:
        orm_mode = True
        extra = "allow"
