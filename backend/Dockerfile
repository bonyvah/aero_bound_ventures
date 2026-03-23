FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app/backend

# Install the application dependencies.
WORKDIR /app/backend
RUN uv sync --frozen --no-cache

# Ensure package imports like `backend.*` resolve correctly.
ENV PYTHONPATH=/app

# Run the application.
CMD ["/app/backend/.venv/bin/uvicorn", "backend.main:app", "--port", "80", "--host", "0.0.0.0"]