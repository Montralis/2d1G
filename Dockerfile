FROM python:3.8-slim-buster
WORKDIR /app
COPY backend backend
COPY frontend frontend
WORKDIR /app/backend
RUN pip install -r requirements.txt
CMD python main.py
