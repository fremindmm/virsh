#!/usr/bin/bash

virsh define /etc/libvirt/qemu/winxp2.xml  #define a unstart virtual machine
virsh start winxp2
virsh list
