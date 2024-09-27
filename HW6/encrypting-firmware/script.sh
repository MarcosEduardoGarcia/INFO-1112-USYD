#!/bin/bash

FIRMWARE_KEY='eeN6Uexa'

#Extract first 72 bytes
head -c72 $1 > encabezado.bin
#xxd -b encabezado.bin

# Data extracted
dd if="$1" of="temp.bin" bs=1 skip=72 status=none
#xxd -b temp.bin

# Encrypted
openssl enc -aes-256-cbc -iter 10 -k "$FIRMWARE_KEY" -in temp.bin -out enc.bin
#xxd -b enc.bin

# Final Firmware
rm $1
cat encabezado.bin enc.bin > $1