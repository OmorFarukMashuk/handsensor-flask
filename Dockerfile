FROM python:3.10-slim-buster

WORKDIR /app

COPY ./src/model /app/src/model/
COPY ./src/service /app/src/service/
COPY ./src/utils /app/src/utils/
COPY ./src/api/app.py /app/src/
COPY requirements.txt /app/

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/app.py"]