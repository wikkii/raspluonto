#!/bin/bash
# Connects to Sonera mobile network.
# Note: Make sure the SIM800 module is powered on!
	sudo /home/pi/sakis/sakis3g connect --console --nostorage --pppd APN="internet" BAUD=9600 CUSTOM_TTY="/dev/ttyAMA0" MODEM="OTHER" OTHER="CUSTOM_TTY" APN_USER="" APN_PASS="" SIM_PIN="" --noprobe
