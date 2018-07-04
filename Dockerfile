FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y locales
RUN apt-get install -y python3-pip python-dev build-essential

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING=UTF-8

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5002

CMD ["python3", "app.py"]