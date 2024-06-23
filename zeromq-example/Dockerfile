FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY client.py ./
COPY server.py ./

RUN pip install --no-cache-dir -r requirements.txt