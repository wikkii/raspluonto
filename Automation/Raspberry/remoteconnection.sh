#!/bin/bash
# Script for creating a reverse SSH tunnel from Raspberry Pi to the server

        ssh -f -N -o BatchMode=yes -R 2222:localhost:22 markus@139.59.140.158
