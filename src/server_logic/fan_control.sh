#!/bin/bash

# Pastikan ipmitool terinstal di Ubuntu 18.04
# sudo apt install ipmitool -y

TEMP=$(cat /sys/class/thermal/thermal_zone0/temp | cut -c1-2)

echo "[*] Suhu Saat Ini: $TEMP C"

if [ "$TEMP" -gt 65 ]; then
    echo "[🚨] Suhu Panas! Memutar Kipas 100% (Full Blast)..."
    # Perintah IPMI standar untuk memaksa kipas full speed
    sudo ipmitool raw 0x30 0x30 0x01 0x00
else
    echo "[✔] Suhu Stabil. Mode Kipas Otomatis (Quiet)."
    # Kembali ke kontrol otomatis BIOS
    sudo ipmitool raw 0x30 0x30 0x01 0x01
fi
