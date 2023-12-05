FROM python:3.8
ADD main.py .
RUN apt-get update && \
pip install --upgrade pip &&\
pip install requests 

CMD ["python", "./main.py"]