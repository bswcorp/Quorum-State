# 🧱 PROTOKOL KEAMANAN FISIK (PHYSICAL SECURITY PROTOCOL)
**Lokasi Utama:** Genesis Node Lab (Ciracas / BreSpeedWorks)
**Prinsip:** Perlindungan Lapis Baja untuk Aset Kritis.

---

### 1. PERLINDUNGAN SERVER & HARDWARE (IBM x3650)
*   **Akses Terbatas:** Hanya Founder (Capo) dan teknisi terverifikasi yang boleh menyentuh fisik server.
*   **Power Stability:** Penggunaan UPS (Uninterruptible Power Supply) untuk mencegah kerusakan komponen akibat mati lampu mendadak (Sangat krusial untuk server "Aki-Aki").
*   **Port Locking:** Penutupan port USB dan VGA yang tidak digunakan guna mencegah akses fisik langsung oleh pihak luar.

### 2. MANAJEMEN SEED PHRASE & PRIVATE KEY (COLD STORAGE)
*   **Anti-Digital:** DILARANG menyimpan Seed Phrase atau Private Key di HP Xiaomi, Cloud (Google Drive/iCloud), atau dalam bentuk foto/screenshot.
*   **Metode Cadangan Fisik:**
    *   **Steel Plate:** Kunci pemulihan dicetak/diukir pada pelat baja tahan karat untuk perlindungan dari kebakaran dan banjir.
    *   **Split Seed:** Membagi kata kunci menjadi dua bagian dan menyimpannya di dua lokasi fisik yang berbeda dan sangat rahasia.
*   **Safety Box:** Penggunaan brankas fisik yang tertanam di lantai atau dinding untuk menyimpan cadangan dompet utama.

### 3. KEAMANAN PERANGKAT MOBILE (MOBILE ENDPOINT)
*   **HP Xiaomi Security:** Mengaktifkan enkripsi penuh pada perangkat, pola kunci yang rumit, dan fitur *Remote Wipe* jika HP hilang atau dicuri.
*   **Sim Swap Protection:** Menggunakan verifikasi 2FA berbasis aplikasi (Google Authenticator) daripada SMS untuk menghindari pembajakan nomor HP.

### 4. MITIGASI BENCANA (DISASTER RECOVERY)
*   **Off-site Backup:** Seluruh dokumentasi GitHub dicadangkan secara offline di drive eksternal yang disimpan di luar lokasi Lab Ciracas.
*   **Fire Suppression:** Penyediaan alat pemadam api ringan (APAR) tipe CO2 di dekat rak server IBM guna memadamkan api tanpa merusak sirkuit elektronik.

---

### 5. PERNYATAAN KEDAULATAN FISIK
"Keamanan Quorum-State tidak hanya hidup di dalam baris kode, tetapi juga dijaga oleh kewaspadaan fisik kami. Kami menjaga kunci masa depan dengan disiplin baja."

---
*Diterbitkan oleh: BreSpeedWorks Labs Security & Infrastructure Division*
