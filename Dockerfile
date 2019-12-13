FROM python:3.6

ADD src /app
WORKDIR /app
ADD schema.json schema.json
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt -t .