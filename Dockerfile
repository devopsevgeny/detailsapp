FROM python:3.11-slim AS base

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1

# Builder stage
FROM base AS builder

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc git curl && \
    pip install --no-cache-dir pipenv==2023.11.15 && \
    PIPENV_VENV_IN_PROJECT=1 pipenv sync && \
    rm -rf /root/.cache && \
    apt-get purge -y gcc git && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/*

# Runtime stage
FROM base AS runtime

RUN useradd -m -d /home/app -s /bin/bash app_user

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY details.py gunicorn_conf.py ./
COPY src/ src/

RUN chown -R app_user:app_user /app

USER app_user

EXPOSE 8000

CMD ["/app/.venv/bin/gunicorn", "--config", "/app/gunicorn_conf.py", "src.details:app"]
