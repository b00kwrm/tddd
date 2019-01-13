FROM debian:latest

COPY . /tmp

WORKDIR /tmp

RUN apt-get update && apt-get upgrade -y && apt-get install rsyslog python3 -y

RUN /etc/init.d/rsyslog start

RUN python3 /tmp/cron_test.py

# keep docker image running
CMD tail -f /dev/null