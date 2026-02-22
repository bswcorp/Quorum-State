# 🛠️ JADWAL PERAWATAN RUTIN (PREVENTIVE MAINTENANCE)
**Unit:** IBM System x3650 M2 & M3 (Genesis Node 01 & 02)  
**Status:** Post-Upgrade (Dual Xeon X5690 + 192GB RAM)  
**Goal:** Uptime 99.9% & Masa Pakai Hardware s/d 2030

---

## 🕒 1. PEMERIKSAAN HARIAN (DAILY CHECK) - [SETIAP SAHUR/PAGI]
*   **Status LED:** Pastikan panel depan tetap **HIJAU** (No Amber/Orange Light).
*   **Temperature Monitor:** Cek via Ubuntu Terminal (`sensors`). Target: < 60°C.
*   **Sync Status:** Pastikan 676 Computors tetap sinkron di `dashboard_simulation.py`.

## 📅 2. PEMERIKSAAN MINGGUAN (WEEKLY CHECK) - [SETIAP JUMAT]
*   **Physical Dusting:** Bersihkan debu pada *Air Intake* (lubang udara depan) dengan vacuum mini/kuas.
*   **Log Audit:** Cek `dmesg` dan `/var/log/syslog` untuk deteksi dini *Hardware Error*.
*   **UPS Test:** Pastikan baterai UPS cadangan terisi 100% untuk antisipasi mati lampu Bintaro.

## 🗓️ 3. PEMERIKSAAN BULANAN (MONTHLY DEEP CLEAN)
*   **Fan Inspection:** Pastikan tidak ada suara kasar pada 10 kipas internal IBM.
*   **Disk Health:** Jalankan `smartctl` untuk cek sisa umur (Life Span) SSD Enterprise.
*   **Backup Config:** Ekspor konfigurasi BIOS dan OS ke Shared Drive `02_INFRASTRUCTURE_TECH`.

## 🍂 4. PEMERIKSAAN SEMESTERAN (SEMI-ANNUAL OVERHAUL)
*   **Thermal Paste:** Aplikasi ulang **Arctic MX-6** pada Dual Processor (Setiap 6 bulan).
*   **Firmware Update:** Cek pembaruan IMM/BIOS di [IBM Support Portal](https://www.ibm.com).
*   **Stress Test:** Jalankan ulang pengujian beban selama 2 jam untuk memastikan stabilitas RAM 192GB.

---

### 🚦 PROTOKOL DARURAT (EMERGENCY)
Jika suhu melampaui **75°C** atau terdengar bunyi alarm panjang (Beep):
1.  Jalankan **Emergency Shutdown Procedure** (Sesuai draf kita sebelumnya).
2.  Putuskan aliran listrik utama.
3.  Hubungi Teknisi RS Server untuk klaim garansi 30/90 hari.

---
**"Aset Terawat adalah Keuntungan yang Terjamin."**

**CAPO** | *Head of Infrastructure* | **BreSpeedWorks Labs**
