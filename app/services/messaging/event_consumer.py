import json
import logging
import asyncio
import aio_pika

from app.core.rabbit import get_rabbitmq_connection
from app.services.notification import send_notification
from app.core.logging import setup_logging

logger = logging.getLogger(__name__)


async def process_message(message: aio_pika.IncomingMessage) -> None:
    async with message.process():
        event = json.loads(message.body.decode())
        logger.info(f'[x] Received event: {event}')

        try:
            await send_notification(event['user_id'], event['type'], event['data'])
        except Exception as err:
            logger.critical(f'[x] Error processing message: {err}')
            return False


async def start_consumer(queue_name: str = 'notifications_queue') -> None:
    async with get_rabbitmq_connection() as connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=100)

        queue = await channel.declare_queue(queue_name, durable=True)

        logger.info('[*] Waiting for messages. To exit press CTRL+C')
        await queue.consume(process_message)
        await asyncio.Future()  # infinite cycle


if __name__ == "__main__":
    setup_logging()
    exit_code = 0 if asyncio.run(start_consumer()) else 1
    exit(exit_code)