FROM debian:latest

RUN apt-get update
RUN apt-get install -y python3 git python3-pip

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["run.py"]

EXPOSE 5000
