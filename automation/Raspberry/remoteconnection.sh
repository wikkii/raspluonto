#!/bin/bash
# Script for creating a reverse SSH tunnel from Raspberry Pi to the server

#output=$(netstat | awk '$5 ~ /^139.59.140.158:ssh/ && $6 ~ /ESTABLISHED/')     # NOT RELIABLE AS IT IS! Just run the ssh command by itself.
#connection=$output

#if [ "$connection" ]; then
#:
#else
ssh -f -N -o BatchMode=yes -R 2222:localhost:22 markus@139.59.140.158
#fi
