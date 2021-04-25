FROM python:3.6-alpine
MAINTAINER rohit.kuru@gmail.com

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN dos2unix entrypoint.sh

CMD ["sh","entrypoint.sh"]