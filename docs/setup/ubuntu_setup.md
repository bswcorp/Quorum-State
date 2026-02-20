# 🐧 PANDUAN INSTALASI & OPTIMASI UBUNTU SERVER (QUORUM-STATE)

Dokumen ini adalah standar operasional prosedur (SOP) untuk instalasi node **Quorum-State ($QSTATE)** pada lingkungan Linux Ubuntu.

---

## 1. Spesifikasi Target
*   **OS:** Ubuntu Server 18.04 LTS / 20.04 LTS / 22.04 LTS.
*   **Hardware:** IBM System x3650 M3 / x3250 M2 / VPS Cloud.
*   **Minimal RAM:** 4GB (8GB+ Disarankan untuk AI Training).

## 2. Langkah Instalasi "Anti-Macet"
1.  **Booting:** Masukkan USB/DVD Installer.
2.  **Edit Boot (Opsi):** Jika layar putih/macet, tekan `e` pada menu installer, cari `quiet splash`, tambahkan `nomodeset`.
3.  **Minimal Install:** Pilih opsi instalasi minimal (tanpa GUI) untuk performa maksimal.
4.  **Network:** Pastikan OpenSSH Server dicentang untuk akses remote dari HP Xiaomi.

## 3. Konfigurasi Pasca-Instalasi (Terminal)

### A. Update Sistem & Dependensi
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git ipmitool -y
