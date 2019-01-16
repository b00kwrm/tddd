FROM debian:latest
COPY . /tmp
WORKDIR /tmp
RUN apt-get update && apt-get upgrade -y && apt-get install sudo rsyslog python3 -y
CMD /bin/bash /tmp/start-stuff.sh
