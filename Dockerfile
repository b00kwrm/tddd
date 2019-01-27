FROM debian:latest
COPY ./start-stuff.sh /tmp
COPY ./bash_timestamp.sh /etc/profile.d/
WORKDIR /tmp
RUN apt-get update && apt-get upgrade -y && apt-get install sudo rsyslog python3 openssh-server -y
RUN adduser --disabled-password --gecos "" oracle && echo "oracle:ginger" | chpasswd
CMD /bin/bash /tmp/start-stuff.sh
