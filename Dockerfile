FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

COPY pyproject.toml README.md ./

RUN pip install --upgrade pip && \
    pip install .[dev]

COPY backend ./backend
COPY frontend-htmx ./frontend-htmx

ENV PYTHONPATH="/app/backend"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
