#!/bin/bash

/etc/init.d/rsyslog start
/etc/ini.d/ssh start
/etc/init.d/cron restart
python3 /tmp/cron_test.py
tail -f /dev/null
