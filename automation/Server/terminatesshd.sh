#!/bin/bash

CheckPID=$(sudo lsof -ti TCP:2222)
PID=$CheckPID

CheckSession=$(who)
session=$CheckSession

#CheckSession = $(ps aux | grep '[m]arkus@pts/0')
#session = $CheckSession

if [ "$session" ]; then
:
#echo 'Someone is logged in! Aborting...'

else
ps aux | grep 'sshd: markus' | awk '{print $2}' | grep -v $PID | sudo xargs kill -9
#echo 'Just killed all processes!'

fi
