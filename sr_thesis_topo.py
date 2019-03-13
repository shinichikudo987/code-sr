#!/usr/bin/env python
"""Custom topology
5 routers in 5 cities, 3 hosts.
"""
from mininet.topo import Topo
class SRTopo( Topo ):
"Simple topology."
def __init__( self ):
"Create custom topo."
# Initialize topology
Topo.__init__( self )
# Add hosts and switches
host1 = self.addHost( 'h1' )
host2 = self.addHost( 'h2' )
host3 = self.addHost( 'h3' )
s1 = self.addSwitch('s1')
s2 = self.addSwitch('s2')
s3 = self.addSwitch('s3')
s4 = self.addSwitch('s4')
s5 = self.addSwitch('s5')
# Add links for hosts
self.addLink( host1, s1, delay='5ms' )
self.addLink( host2, s5, delay='5ms' )
self.addLink( host3, s1, delay='5ms' )
# Add links between switches
# Only a single link will be added here between any pair of switches
# Extra links will be added by the script that imports this topo file
# See sr_mn_script.py
self.addLink( s1, s2, delay='10ms' )
self.addLink( s1, s3, delay='15ms' )
self.addLink( s1, s4, delay='10ms' )
self.addLink( s2, s3, delay='500ms' )
self.addLink( s3, s4, delay='50ms' )
self.addLink( s3, s5, delay='20ms' )
self.addLink( s4, s5, delay='100ms' )
topos = { 'mytopo': ( lambda: SRTopo() ) }

