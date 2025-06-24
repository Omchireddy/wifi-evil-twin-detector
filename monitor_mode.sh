#!/bin/bash

if [ "$1" == "start" ]; then
    echo "[*] Enabling monitor mode on wlan0..."
    sudo airmon-ng start wlan0
elif [ "$1" == "stop" ]; then
    echo "[*] Disabling monitor mode on wlan0mon..."
    sudo airmon-ng stop wlan0mon
else
    echo "Usage: ./monitor_mode.sh [start|stop]"
fi
