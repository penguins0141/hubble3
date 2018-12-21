#!/bin/bash

for hostname in $(cat icq-srv.txt);do

host $hostname | grep "has address"

done

