import asyncio
from alembic import context
from sqlmodel import SQLModel
from logging.config import fileConfig
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import AsyncEngine

from app.core.session import engine 
from app.core.settings import settings

from app.applications.events.models import Notification

# this is the Alembic Config object, which we get from the file configuration.
config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_scheme="postgresql+asyncpg",
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine

    if isinstance(connectable, AsyncEngine):
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)
    else:
        with connectable.connect() as connection:
            do_run_migrations(connection)


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())