from datetime import datetime
from pydantic import BaseModel, Field

class Note(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    tags: list[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)