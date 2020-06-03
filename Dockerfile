FROM python:3.7

ADD src /app
WORKDIR /app
ADD schema.json schema.json
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt -t .

ENTRYPOINT [ "python" ]