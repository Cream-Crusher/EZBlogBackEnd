import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class BlogBase(BaseModel):
    title: str = Field(default=None, max_length=250)
    description: str = Field(default=None)
    active: bool


class BlogRead(BlogBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class BlogCreate(BlogBase):
    owner_id: uuid.UUID


class BlogUpdate(BlogBase):
    pass
