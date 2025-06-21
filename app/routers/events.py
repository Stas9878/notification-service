from fastapi import APIRouter
from app.schemas.event import EventMessage
from app.services.messaging.event_producer import send_event_to_queue

router = APIRouter(tags=['Events'])


@router.post('/')
async def handle_event(event: EventMessage) -> dict[str, str]:
    await send_event_to_queue(event)
    return {'status': 'Event queued'}