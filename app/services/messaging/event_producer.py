import logging
import aio_pika

from app.core.rabbit import get_rabbitmq_connection
from app.schemas.event import EventMessage

logger = logging.getLogger(__name__)


async def send_event_to_queue(event: EventMessage, queue_name: str = 'notifications_queue') -> None:
    async with get_rabbitmq_connection() as connection:
        channel = await connection.channel()
        await channel.declare_queue(queue_name, durable=True)

        body = event.model_dump_json().encode()
        await channel.default_exchange.publish(
            aio_pika.Message(body=body),
            routing_key=queue_name,
        )
        logger.info(f'[x] Sent event {event.type} with body {body} to queue')