#! /bin/bash

## fidi Driver
modprobe ftdi-sio

## cardio help usb adapter 
echo 0403 9A48 > /sys/bus/usb-serial/drivers/ftdi_sio/new_id
