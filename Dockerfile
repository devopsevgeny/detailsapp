FROM python:3.12-slim AS base

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

# Install pipenv and build tools
FROM base AS builder

RUN apt-get update && apt-get install -y --no-install-recommends gcc pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync --deploy --ignore-pipfile && \
    rm -rf /root/.cache

FROM base AS runtime

# Create app user
RUN useradd -m -d /home/app -s /bin/bash app_user

WORKDIR /home/app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /home/app/.venv

# Copy project files
COPY details.py gunicorn_conf.py ./
COPY src/ src/

USER app_user

# Run via Gunicorn
CMD [ "/home/app/.venv/bin/gunicorn", "--config", "/home/app/gunicorn_conf.py", "src.details:app" ]

