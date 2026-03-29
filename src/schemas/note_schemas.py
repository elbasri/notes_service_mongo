from pydantic import BaseModel, Field
import datetime

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)
    tags: list[str] = []
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    class Config:
        orm_mode = True


class NoteRead(BaseModel):
    id: str
    title: str
    content: str
    tags: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime | None = None

    class Config:
        orm_mode = True