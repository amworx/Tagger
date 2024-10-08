FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN python -m app.initialize_db && python app.py

COPY . .

EXPOSE 5000

RUN python initialize_db.py && python app.py