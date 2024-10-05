FROM python:3.12

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env .
COPY main.py .
COPY ./config ./config
COPY ./models ./models
COPY ./routes ./routes
COPY ./schema ./schema