#!/bin/bash
# Checks whether paho-mqtt-client is running or not. If it isn't, then restart $
# This script is run every 10 minutes by cron.

output=$(pgrep -fn paho-mqtt-client.py)
testi=$output

if [ "$testi" ]; then
:
else
python /home/markus/paho-mqtt/paho-mqtt-client.py >/dev/null &
fi
