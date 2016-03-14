#!/usr/bin/env python
#coding=utf-8
import libvirt

conn = libvirt.open('remote43')

for id in conn.listDomainsID():
    dom = conn.lookupByID(id)
    print "dom %s State %s" % (dom.name(), dom.info())
    dom.suspend()
    print "dome %s State %s" % (dom.name(), dom.info()[0])
    dom.resume()
    print "dome %s State %s" % (dom.name(), dom.info()[0])
    dom.destroy()
    print "dome %s State %s" % (dom.name(), dom.info()[0])

