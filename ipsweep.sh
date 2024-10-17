#!/usr/bin/env bash


echo '--------------------------------------------------'
echo 'Give IP for Sweep (e.g., 192.168.1):'
echo '--------------------------------------------------'
read a

if [ "$a" == "" ]; then
    echo "You forgot to provide an IP address!"
    echo "Syntax: ./ipsweep.sh 192.168.1"
    exit 1
else
    for ip in $(seq 1 254); do
        echo '--------------------------------------------------'
        echo "Pinging IP: $a.$ip"
        echo '--------------------------------------------------'

        # Perform ping and check if the host is up
        if ping -c 1 -W 1 $a.$ip > /dev/null 2>&1; then
            echo '--------------------------------------------------'
            echo "Response from $a.$ip: Host is UP"
            echo '--------------------------------------------------'
        else
            echo '--------------------------------------------------'
            echo "No response from $a.$ip: Host is DOWN"
            echo '--------------------------------------------------'
        fi
    done
fi
