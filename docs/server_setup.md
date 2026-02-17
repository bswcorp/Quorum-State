# 🖥️ Panduan Instalasi Server Genesis: IBM x3650

Dokumen ini berisi spesifikasi dan langkah awal untuk menjalankan node **Quorum-State** pada infrastruktur server fisik.

## 1. Spesifikasi Minimum (Recomended)
- **OS:** Ubuntu Server 22.04 LTS atau 24.04 LTS (Lightweight & Stable).
- **CPU:** Dual Intel Xeon (Optimal untuk pemrosesan Quorum paralel).
- **RAM:** Minimum 16GB (Untuk menangani memori simulasi kuantum).
- **Storage:** SAS/SSD dengan konfigurasi RAID untuk redundansi data ledger.

## 2. Dependensi Perangkat Lunak
Instalasi awal yang diperlukan melalui terminal:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3-pip python3-venv build-essential -y
