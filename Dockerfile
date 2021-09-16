FROM python:3.8-slim-buster
WORKDIR /app
COPY backend backend
COPY frontend frontend
RUN pip3 install -r backend/requirements.txt
CMD python backend/main.py
