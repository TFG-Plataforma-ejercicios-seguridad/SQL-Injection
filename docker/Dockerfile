# syntax=docker/dockerfile:1
FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git postgresql-dev gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base

RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install ipdb
RUN pip install ipython

WORKDIR /app

RUN git clone https://github.com/TFG-Plataforma-ejercicios-seguridad/SQL-Injection.git .
RUN pip install -r requirements.txt

WORKDIR /app/ejercicioSQL

COPY docker-settings.py /app/ejercicioSQL/local_settings.py

RUN ./manage.py collectstatic

#CMD ["gunicorn", "-w 5", "ejercicioSQL.wsgi", "--timeout=500", "-b 0.0.0.0:5000"]