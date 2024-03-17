FROM python:3.12.1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
COPY database.py .
COPY model.py .

COPY alembic/ alembic
COPY alembic.ini .

RUN alembic upgrade head

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]