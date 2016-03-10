#!/usr/bin/bash

domain='winxp2'
qemu-img create -f qcow2 /var/lib/libvirt/images/${domain}.qcow2 10G #create a xishu file

virsh define /etc/libvirt/qemu/${domain}.xml  #define a unstart virtual machine
virsh start ${domain}  # start a unstart vm

virsh list  #list all vm
virsh suspend ${domain}
virsh list
virsh resume  ${domain}
virsh list
virsh destroy ${domain}
virsh list
