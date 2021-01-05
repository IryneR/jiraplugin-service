#FROM python:3
#WORKDIR /src/api
#COPY api.py .
#CMD ["python", "/api.py"]


#FROM python:3.7-alpine
#WORKDIR /src/api
#ENV FLASK_APP=api.py
#ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#EXPOSE 5000
#COPY . .
#CMD ["flask", "run"]


#$ cat my_flask_app/Dockerfile
#FROM ubuntu:latest
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#COPY . /api
#WORKDIR /api
#RUN pip install -r requirements.txt
#ENTRYPOINT ['python']
#CMD ['api.py']


#create an image and container but doesn't work corectly
FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
#We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /api/requirements.txt
WORKDIR /api
RUN pip install -r requirements.txt
COPY . /api
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]


#FROM python:3.8
# set the working directory in the container
#WORKDIR /code
# copy the dependencies file to the working directory
#COPY requirements.txt .
# install dependencies
#RUN pip install -r requirements.txt
# copy the content of the local src directory to the working directory
#COPY src/ .
# command to run on container start
#CMD [ "python", "./server.py" ]