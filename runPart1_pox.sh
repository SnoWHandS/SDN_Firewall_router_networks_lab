#!/bin/bash
cp firewall/firewall-policies.csv ~/pox/pox/forwarding/
cp l2_learning.py ~/pox/pox/forwarding/

cd ~/pox
./pox.py forwarding.l2_learning
