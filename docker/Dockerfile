FROM debian:latest
COPY docker/mimikatz /tmp
COPY docker/cron_test.py /tmp
COPY docker/start-stuff.sh /tmp
COPY docker/bash_timestamp.sh /etc/profile.d/
WORKDIR /tmp
RUN apt-get update && apt-get upgrade -y && apt-get install sudo rsyslog python3 openssh-server rsync -y
CMD /bin/bash /tmp/start-stuff.sh
