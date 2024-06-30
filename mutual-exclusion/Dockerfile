FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY client.py ./
COPY coordinator.py ./

RUN pip install --no-cache-dir -r requirements.txt