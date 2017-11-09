#!/bin/bash
# Script for killing old connections to port 2222. Run this after remote connection is over.
# Note! This is run on the server! You can check if (CLOSE WAIT) connections are still alive with: "sudo lsof -i TCP:2222".

sudo lsof -t -i tcp:2222 -s tcp:listen | sudo xargs kill
