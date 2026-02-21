# 🚨 PROSEDUR PENGHENTIAN DARURAT (EMERGENCY SHUTDOWN PROCEDURE)
**Project:** Quorum-State ($QSTATE)  
**Status:** Top Priority Security Protocol  
**Trigger:** Serangan Siber (Exploit/DDoS), Gangguan Fisik (Kebakaran), atau Malfungsi Node Genesis.

---

### 1. IDENTIFIKASI KRISIS (CRISIS IDENTIFICATION)
Prosedur ini wajib dieksekusi JIKA terjadi salah satu kondisi berikut:
1. **Critical Vulnerability:** Ditemukan celah yang memungkinkan pengurasan dana Treasury atau manipulasi Ledger secara masif.
2. **51% Attack:** Terdeteksi upaya pengambilalihan konsensus oleh pihak yang tidak sah.
3. **Physical Threat:** Kebakaran, banjir, atau upaya pencurian fisik di Lab Ciracas (IBM x3650).
4. **Legal Halt:** Perintah resmi dari otoritas hukum (London/Silicon Valley/BAPPEBTI) untuk pembekuan sementara.

### 2. LANGKAH EKSEKUSI (STEP-BY-STEP ACTION)

#### FASE 1: ISOLASI JARINGAN (NETWORK ISOLATION)
*   **Action:** Putuskan koneksi internet pada server IBM x3650.
*   **Method:** Cabut kabel LAN atau matikan switch/router di Lab Ciracas.
*   **Goal:** Menghentikan komunikasi antar-node dan mencegah keluarnya data/dana secara ilegal.

#### FASE 2: PENGHENTIAN LAYANAN (SERVICE HALT)
*   **Action:** Hentikan proses node Quorum secara paksa.
*   **Terminal Command (via HP Xiaomi/SSH):** 
    ```bash
    taskkill /F /IM quorum.exe  # (Untuk Windows Server 2012 R2)
    ```
*   **Goal:** Memastikan tidak ada blok baru yang dihasilkan selama investigasi.

#### FASE 3: PENGAMANAN ASET (ASSET PROTECTION)
*   **Action:** Amankan Hardware Wallet dan Steel Plate Seed Phrases ke lokasi cadangan rahasia (Sesuai Protokol Keamanan Fisik).
*   **Action:** Cabut kabel power server IBM untuk mencegah kerusakan komponen akibat lonjakan listrik saat krisis.

---

### 3. PROTOKOL KOMUNIKASI & PEMULIHAN (RECOVERY)
1. **Public Announcement:** Kirim notifikasi "Maintenance Darurat" melalui Landing Page dan Media Sosial untuk menjaga transparansi (Tanpa membocorkan detail teknis celah).
2. **Snapshot:** Lakukan *Backup/Snapshot* pada data Ledger terakhir yang valid sebelum serangan terjadi.
3. **Post-Mortem Analysis:** Lakukan audit menyeluruh berdasarkan **NIST Audit Checklist** untuk menemukan akar masalah.
4. **Re-Activation:** Jaringan hanya boleh dinyalakan kembali setelah verifikasi keamanan 100% dan persetujuan dari dewan pengawas.

---
*"Keamanan adalah prioritas di atas kecepatan. Kami lebih memilih menghentikan dunia daripada membiarkan kejahatan menang."*

**BreSpeedWorks Labs Emergency Response Team (ERT)**
