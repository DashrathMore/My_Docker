FROM python:3.8

ADD main.py .

RUN apt-get update


CMD ["python", "./main.py"]
