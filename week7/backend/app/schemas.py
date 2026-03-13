from datetime import datetime

from pydantic import BaseModel

from pydantic import BaseModel, validator

class ActionItemCreate(BaseModel):
    title: str
    description: str | None = None

    @validator("title")
    def title_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        return value

class NoteCreate(BaseModel):
    title: str
    content: str


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None


class ActionItemCreate(BaseModel):
    description: str


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: str | None = None
    completed: bool | None = None


