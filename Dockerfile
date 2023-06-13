FROM python:3-alpine3.15
# FROM alpine:latest
WORKDIR /app
COPY . /app
# RUN pip install -r requirements.txt
# RUN apk add --no-cache --update \
#     python3 python3-dev gcc \
#     gfortran musl-dev

# ADD requirements.txt .
# RUN /env/bin/pip install wheel  
# ENV PIP_WHEEL_DIR=/wheelhouse  
# ENV WHEELHOUSE=/wheelhouse  
# ENV PIP_FIND_LINKS=/wheelhouse 
RUN apk --no-cache add musl-dev linux-headers g++
# RUN pip3 install --upgrade pip setuptools && \
#     pip3 install -r requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD python ./src/app.py