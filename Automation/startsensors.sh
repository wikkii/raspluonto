#!/bin/bash
#This script will be run by cron after starup. 

        python /test_code/mqtt_pir_test.py & python mqtt_flame.py
