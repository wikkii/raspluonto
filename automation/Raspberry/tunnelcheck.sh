#!/bin/bash
# Checks whether a reverse SSH tunnel is up. If not, re-create it.

echo "SSH tunnel status..."
check(){
if [[ $(netstat -lnp | grep ':22') = *ssh* ]]; then
echo "Server-Pi SSH tunnel UP"
else echo "Server-Pi SSH tunnel DOWN, reinstating"
#ssh -f -N -o BatchMode=yes 2222:localhost:22 markus@139.59.140.158
fi
}
check
