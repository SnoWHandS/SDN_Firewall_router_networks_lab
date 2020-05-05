#!/bin/bash

echo "running pox in background and directing output to /dev/null"

(./runPart1_pox.sh &) > /dev/null 2>&1

echo "Launching mininet with topo"
sudo ./firewall/sdn.py

echo "Mininet complete, killing any remaining processes"
pkill -9 runPart1_pox.sh
pkill -9 python2.7

echo "clearing mininet. . ."
(sudo mn -c&) > /dev/null 2>&1
