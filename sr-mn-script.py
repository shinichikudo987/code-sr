#!/usr/bin/env python
'''
A script to connect 5 router & 3 host topo
'''
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import UserSwitch, RemoteController, OVSSwitch
from mininet.topolib import TreeNet
from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.link import TCLink
from functools import partial
from sr_thesis_topo import SRTopo
from alterableNet import alterableCLI
from alterableNet import alterNet
def setDefaultRoute(node, ip, intf=None):
"""
Modified node.setDefaultRoute that sets a default gateway IP.
"""
if not intf:
intf = node.defaultIntf()
node.cmd('route add -net 0.0.0.0 gw %s %s' % (ip, intf))
if __name__ == '__main__':
setLogLevel( 'info' )
topo = SRTopo()
# load the topology specified in sr_thesis_topo.py, use the cpqd1.3 switch and point
to a controller running
# in this VM
# link parameter enables addition of custom link delays
net
=
alterNet(topo=topo,
switch=UserSwitch,
controller=partial(RemoteController,ip='127.0.0.1'), link=TCLink)
# adding extra links between routers and delays
s1, s2, s3, s4, s5 = net.switches
net.addLink( s1, s4, delay='10ms' )
net.addLink( s3, s5, delay='5ms' )
net.start()
# end-host configuration
h1, h2, h3 = net.hosts
# host h1 is attached to router s1 / FICIX
h1.setIP("10.10.1.101/24")
h1.setMAC("00:00:00:00:01:02")
setDefaultRoute(h1, "10.10.1.1")
# host h2 is attached to router s5 / AMSIX
h2.setIP("10.10.2.102/24")
h2.setMAC("00:00:00:00:02:24")
setDefaultRoute(h2, "10.10.2.1")
# host h3 is attached to router s1 / FICIX
h3.setIP("10.10.3.103/24")
h3.setMAC("00:00:00:00:03:12")
setDefaultRoute(h3, "10.10.3.1")
alterableCLI(net)
net.stop()
