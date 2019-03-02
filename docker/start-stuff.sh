#!/bin/bash
/etc/init.d/rsyslog start
/etc/init.d/ssh start
/etc/init.d/cron restart
python3 /tmp/cron_test.py
adduser --disabled-password --gecos "" oracle && echo "oracle:ginger" | chpasswd
addgroup test_group
adduser oracle test_group
apt-get update && apt-get upgrade -y
apt-get install linux-headers-amd64 -y
cat <<EOF > /dev/shm/hello.txt
hello, /dev/shm
EOF
tail -f /dev/null
