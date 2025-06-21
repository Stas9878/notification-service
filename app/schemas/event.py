from pydantic import BaseModel


class EventMessage(BaseModel):
    user_id: int
    type: str
    data: dict