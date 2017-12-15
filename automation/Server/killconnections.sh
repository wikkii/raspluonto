#!/bin/bash
# Script for killing old connections to port 2222. Run this after Raspberry Pi has been restarted.

  sudo lsof -t -i tcp:2222 -s tcp:listen | sudo xargs kill
