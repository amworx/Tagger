FROM python:3.9-slim

WORKDIR /app
RUN python -m initialize_db && python app.py

COPY requirements.txt .

RUN pip install -r requirements.txt
#RUN export PYTHONPATH=$PYTHONPATH:/app && python -m app.initialize_db && python app.py

COPY . .

EXPOSE 5000

RUN python initialize_db.py && python app.py