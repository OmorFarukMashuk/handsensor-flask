FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN apk --no-cache add musl-dev linux-headers g++
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 3000
CMD python ./src/app.py