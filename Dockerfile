#FROM 3.9.1-slim-buster
FROM python:3.7



ADD . /app/
WORKDIR /app

RUN pip install fastapi uvicorn sklearn joblib

EXPOSE 80
CMD ["uvicorn","main:app","--host","0.0.0.0", "--port","80"]

