#!/bin/bash
#This script will be run by cron after starup. 

       python /home/pi/test_code/mqtt_pir_test.py & python /home/pi/test_code/mqtt_flame.py
