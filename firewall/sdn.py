#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo
import time

class Tree(Topo):
    #Override the build method of Topo
    def build(self):
        for host_no in range(1,9):
            self.addHost('h%s'% host_no, mac = '00:00:00:00:00:0%s'% host_no)
        for switch_no in range(1,8):
            self.addSwitch('s%s'%switch_no)

        #1st tier
        self.addLink('s1','s5')
        self.addLink('s1','s2')

        #2nd tier        
        self.addLink('s2','s4')
        self.addLink('s2','s3')

        self.addLink('s5','s7')
        self.addLink('s5','s6')


        #Connect all hosts
        self.addLink('s3','h1')
        self.addLink('s3','h2')

        self.addLink('s4','h3')
        self.addLink('s4','h4')

        self.addLink('s6','h5')
        self.addLink('s6','h6')

        self.addLink('s7','h7')
        self.addLink('s7','h8')

        return
def treeTopo():
    tree_topo = Tree()


    net = Mininet(topo = tree_topo, controller=RemoteController )
    net.start()
    #print("sleeping for 30 seconds to allow hosts to send data to the switch")
    #time.sleep(30)
    print("Pinging all")
    net.pingAll()
    #net.interact()
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
