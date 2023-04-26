# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /notes-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--app", "notes-app:notes_app" "--host=0.0.0.0"]
