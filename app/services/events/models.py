from sqlmodel import Field, SQLModel
from datetime import datetime


class Notification(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int
    type: str
    channel: str
    status: str
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)