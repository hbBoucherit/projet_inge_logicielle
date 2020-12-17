FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN python -m pip install --upgrade pip
RUN pip install typing fastapi numpy sklearn joblib

COPY ./app /app

