#!/bin/bash
#Script for creating a reverse SSH tunnel from Raspberry Pi to the server

createTunnel() {
	/usr/bin/ssh -N -R 2222:localhost:22 markus@139.59.140.158


	if [[ $? -eq 0 ]]; then
		echo Tunnel created successfully
	else
		echo An error occured while creating a tunnel. RC was $?
	fi
}

	/bin/pidof ssh
	
	if [[ $? -ne 0 ]]; then
		echo Creating new tunnel connection
	
		createTunnel
	
fi
