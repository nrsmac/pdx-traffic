FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

ENV DAGSTER_HOME /dagster_home
CMD ["uv", "run", "dagster", "dev", "--host", "0.0.0.0"]