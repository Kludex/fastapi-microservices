FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

ENV PYTHONPATH /

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm /app/requirements.txt

COPY ./app /app
