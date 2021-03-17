FROM python:3.6.4

WORKDIR /sales-managment-app

COPY . /sales-managment-app

RUN pip install -r requirements.txt
