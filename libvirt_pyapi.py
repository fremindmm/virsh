#!/usr/bin/python
#Get domain info via libvirt python API.
#Tested with python2.6 and libvirt-python-1.17 on a KVM host.

import libvirt
import sys

def createConnection():

