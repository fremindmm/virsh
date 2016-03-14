#!/usr/bin/bash

img_des_dir="/var/lib/libvirt/images"
img_name="template"
domain="template"
domain_conf="/etc/libvirt/qemu/${domain}.xml"
function create_img()
{
    cd ${img_des_dir}
    qemu-img create -f qcow2 ${template}.qcow2 3G
}

function define_domain()
{
    virsh define $1
}

function start_domain()
{
    virsh start $1
}

function suspend_domain()
{
    virsh suspend $1
}

function resume_domain()
{
    virsh resume $1
}

function destroy_domain()
{
    virsh destroy $1
}

function query_domain_list()
{
    virsh list --all
}

function main()
{
    create_img
    define_domain ${domain_conf}
    start_domain ${domain}
    query_domain_list
    suspend_domain ${domain}
    query_domain_list
    resume_domain ${domain}
    query_domain_list
    destroy_domain ${domain}
    query_domain_list ${domain}
}
main
