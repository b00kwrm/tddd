#!/bin/bash

/etc/init.d/rsyslog start
/etc/init.d/ssh start
/etc/init.d/cron restart
python3 /tmp/cron_test.py
apt-get install linux-headers-$(uname -r)
tail -f /dev/null
