#!/bin/bash
#This script will be run by cron after startup. 

       python /home/pi/test_code/mqtt_pir_test.py & python /home/pi/test_code/flame_test.py
