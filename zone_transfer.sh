#!/bin/bash

echo "[*] Please enter domain name:"
read domain

for fqdn in $(host -t ns $domain |cut -d" " -f4); do
host -l $domain $fqdn |grep "has address"
done