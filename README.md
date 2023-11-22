# docker_flask_homework

## Part 1.
To dockerize the app, we created a file with the following commands:

FROM python:3.7-alpine: this command what it does is going to dockerhub and look for a command 
WORKDIR /app: This is the working directory of the app.
COPY . /app: this what is does basically is take everything in app.py, docketfile and requirements txt and pt it together in a new file callled application.
EXPOSE 5000: this is the port in which we are running the app.
CMD ["python", "app.py"]: this is the command we use to run an app in python. 

To run this app with docker:
* First, we need to create an image with: docker build -t alexa .
* second, verifying the image was create: docker images
* third: to run the app with docker: docker run -p 8005:5000 alexa
* to stop the app: control + C

Challenges faced:
The mayor challenge with this assigment was to send the changes to github. I had to repeat the processof creating a token and installing it in google shell. 

## Part 2.

In order to run thee two apps simultaneously, we need a file called docker-compose.yaml
This file contains:
* Services: here each service is defined, alomg with its configuartion.
* Networks: indicates the newtwork the container will use to communicate.
* Volumes: establish persistent storage of the container. 

Important commands in docker-compose:
* docker-compose build: to create an image
