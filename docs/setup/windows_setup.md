# 🪟 PANDUAN INSTALASI & PENGAMANAN WINDOWS SERVER (QUORUM-STATE)

Dokumen ini berisi prosedur standar (SOP) untuk menjalankan node **Quorum-State ($QSTATE)** di lingkungan Windows Server.

---

## 1. Spesifikasi Target
*   **OS:** Windows Server 2012 R2 (Standard/Datacenter).
*   **Hardware:** IBM System x3650 M3 / x3250 M2.
*   **Mode Rufus:** MBR (Legacy BIOS Support).

## 2. Langkah Instalasi "Anti-Layar Putih"
1.  **Booting:** Gunakan DVD-RW atau USB Rufus (Mode MBR).
2.  **Driver:** Pastikan Driver Matrox G200 (Video) dan ServeRAID M5015 terinstal sempurna.
3.  **Minimal UI:** Matikan fitur visual yang tidak perlu untuk menghemat RAM.

## 3. Konfigurasi Lingkungan (Environment)

### A. Instalasi Python & Git
1.  Unduh **Python 3.10+** (Centang "Add Python to PATH").
2.  Unduh **Git for Windows** untuk sinkronisasi repositori.

### B. Sinkronisasi Proyek
```powershell
git clone https://github.com
cd Quorum-State
