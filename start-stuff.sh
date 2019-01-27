#!/bin/bash

echo 'export HISTTIMEFORMAT="%s "' >> ~/.bashrc
source ~/.bashrc
/etc/init.d/rsyslog start
/etc/init.d/ssh start
/etc/init.d/cron restart
python3 /tmp/cron_test.py
apt-get update && apt-get upgrade -y
apt-get install linux-headers-amd64 -y
tail -f /dev/null
