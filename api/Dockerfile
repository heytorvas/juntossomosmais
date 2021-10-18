FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN mkdir /usr/src/juntossomosmais/
WORKDIR /usr/src/juntossomosmais/api

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
