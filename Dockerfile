FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Set the module search path
ENV PYTHONPATH=/app

# Run the initialization and then the app
CMD ["bash", "-c", "python initialize_db.py && python app.py"]