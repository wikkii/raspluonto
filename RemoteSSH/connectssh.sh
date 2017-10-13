#!/bin/bash
#Script for creating a reverse SSH tunnel from Raspberry Pi to the server

createTunnel() {
        #-o BatchMode=yes means that ssh will fail if auth keys are not setup correctly. This way it does not keep w$
        /usr/bin/ssh -N -o BatchMode=yes -R 2222:localhost:22 markus@139.59.140.158

        #($?) Expands to the exit status of the most recently executed foreground pipeline. -eq for numeric comparis$
        if [[ $? -eq 0 ]]; then
                echo Tunnel created successfully
        else
                echo An error occured when creating a tunnel. RC was $?
        fi
}

        /bin/pidof ssh

        if [[ $? -ne 0 ]]; then
                echo Creating new tunnel connection

                createTunnel

fi
