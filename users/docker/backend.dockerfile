FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

WORKDIR /app
ENV PYTHONPATH /app
ENV PRE_START_PATH /app/scripts/prestart.sh
ENV WEB_CONCURRENCY 3

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm /app/requirements.txt

COPY ./scripts /app/scripts
COPY ./alembic.ini /app/alembic.ini
COPY ./migrations /app/migrations
COPY ./tests /app/tests
COPY ./app /app/app
