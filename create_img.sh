#!/usr/bin/bash
cd /var/lib/libvirt/images

qemu-img create -f raw template.raw 3G
qemu-img create -f qcow2 template.qcow2 3G


