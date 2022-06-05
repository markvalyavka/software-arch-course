FROM python:3.9.3

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY runserver.py runserver.py

COPY ./logging_service /app/logging_service

CMD ["python3", "runserver.py"]
