FROM python:3.12-slim AS base
WORKDIR /app
# Install curl for uv installer
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Install specific uv version
ARG UV_VERSION=0.7.12
RUN curl -fsSL https://astral.sh/uv/$UV_VERSION/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock /app/

# Cache dependencies during sync
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --compile-bytecode


COPY main.py /app/
COPY backend /app/backend
COPY frontend /app/frontend
COPY entrypoint.sh /app/

RUN chmod +x ./entrypoint.sh
ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["./entrypoint.sh"]