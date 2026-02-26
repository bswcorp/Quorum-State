#!/bin/bash
# 🛡️ THE QUANTUM SHIELD: LOCKDOWN TOTAL
# Hanya mengizinkan akses lokal (LAN Bintaro) & Memblokir IP Asing.

echo "🧱 [SHIELD] Mengaktifkan Firewall Kedaulatan..."
sudo ufw default deny incoming
sudo ufw default deny outgoing

# Izinkan SSH hanya dari IP Lokal (Ganti [IP_LAPTOP_CAPO])
sudo ufw allow from 192.168.1.0/24 to any port 22

# Blokir semua koneksi ke China/Barat (Global Block)
sudo ufw enable
echo "🔒 [STATUS] Bintaro Command Center dalam Mode Siluman."
