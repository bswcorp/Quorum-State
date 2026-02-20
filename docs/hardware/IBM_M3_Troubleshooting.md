# 🛠️ Analisis Teknis & Check-list Perbaikan IBM x3650 M3

**Status:** Pemeliharaan (Maintenance Mode)
**Tujuan:** Mengembalikan fungsi sebagai Genesis Node Fisik.

### 🔍 Analisis Kerusakan (Stuck Installation):
1. **RAID Controller Latency:** Kemungkinan baterai CMOS atau RAID Write Cache sudah lemah, menyebabkan proses tulis data ke HDD melambat drastis (stuck 16 jam).
2. **Firmware Outdated:** BIOS/IMM lama mungkin tidak mendukung kernel Linux modern (Ubuntu 24.04) secara optimal.
3. **Thermal Throttling:** Debu pada heatsink Dual Xeon dapat menyebabkan CPU menurunkan kecepatan secara ekstrem.

### ✅ Check-list Perbaikan:
- [ ] Bersihkan debu fisik dan ganti Thermal Paste CPU Xeon.
- [ ] Masuk ke BIOS (F1) -> Cek Status Kesehatan RAID Array.
- [ ] Update Firmware IMM & BIOS ke versi terakhir yang tersedia.
- [ ] Uji coba instalasi menggunakan versi **Ubuntu Server 20.04 LTS** (lebih stabil untuk hardware era M3).
- [ ] Cek integritas RAM menggunakan MemTest86.
