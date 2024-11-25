#!/bin/bash

read -p "Enter target IP: " target
read -p "Enter domain/workgroup (leave empty if unknown): " domain

if [ -z "$domain" ]; then
    smbclient -L //$target -N
else
    smbclient -L //$target -W $domain -N
fi
