#!/usr/bin/env python
#Get domain info via libvirt python API.
#Tested with python2.6 and libvirt-python-1.17 on a KVM host.

import libvirt
import sys

def createConnection():
    conn = libvirt.openReadOnly(None)
    if conn == None:
        print 'Failed to open connection to QEMU/KVM'
    else:
        print '----Connection is created successfully----'
        return conn

def closeConnection(conn):
    print ''
    try:
        conn.close()
    except:
        print 'Failed to close the connection'
        return 1
    print 'Connection is closed'

def getDomInfoByName(conn, name):
    print ''
    print '------ get domain info by name------'
    try:
        myDom = conn.lookupByName(name)
    except:
        print 'Failed to find the domain with name "%s"' % name
        return 1

    print "Dom id: %d name: %s" % (myDom.ID(), myDom.name())
    print "Dom state: %s" % myDom.state(0)
    print "Dom info: %s" % myDom.info()
    print "memory: %d MB" % (myDom.maxMemory()/1024)
    print "memory status: %s" % myDom.memoryStats()
    print "vCPUs: %d" % myDom.maxVcpus()

def getDomInfoByID(conn, id):
    print ''
    print '------ get domain info by ID -----'
    try:
        myDom = conn.lookupByID(id)
    except:
        print 'Failed to find the domain with ID "%d"' % id
        return 1
    print "Domain is is %d; Name is %s" % (myDom.ID(), myDom.name())

if __name__ == '__main__':
    name1 = "winxp"
    name2 = "notExits"
    id1 = 2
    id2 = 9999
    print "----Get domain info via libvirt python API----"
    conn = createConnection()
    getDomInfoByName(conn, name1)
    getDomInfoByName(conn, name2)
    getDomInfoByID(conn, id1)
    getDomInfoByID(conn, id2)
    closeConnection(conn)



