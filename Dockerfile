FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app
RUN cd .. && python /app/initialize_db.py && cd /app && python app.py