FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# environment settings
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1

# Copy pyproject.toml and uv.lock
COPY pyproject.toml ./
COPY uv.lock ./

# Install dependencies
RUN uv sync --no-install-project

# Copy all project
COPY . ./