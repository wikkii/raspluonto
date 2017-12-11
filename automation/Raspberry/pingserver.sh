#!/bin/bash
#Ping nuotiovahti.info and output to uptime.txt.
ping -c 1 139.59.140.158 | while read pong; do echo "$(date): $pong"; done >> /home/pi/uptime.txt
