# 📋 DAFTAR PERIKSA PENERIMAAN UNIT (HARDWARE ACCEPTANCE CRITERIA)
**Unit:** IBM System x3650 M2 & M3 (Genesis Nodes)  
**Status:** Post-Upgrade Inspection  
**Inspektur:** CAPO | BreSpeedWorks Labs

---

## 🔍 I. VERIFIKASI IDENTITAS & FISIK
*   [ ] **1. Serial Number (S/N):** Cocokkan nomor seri di casing dengan nota pembelian & stiker aset.
*   [ ] **2. Kebersihan Internal:** Buka tutup atas, pastikan tidak ada debu tebal, kabel tertata rapi, dan tidak ada bekas korosi/karat.
*   [ ] **3. Thermal Management:** Pastikan *Heatsink* terpasang kencang dan thermal paste (Arctic MX-6) sudah diaplikasikan ulang pada Dual Xeon.

## ⚙️ II. VERIFIKASI BIOS & HARDWARE (SOFTWARE CHECK)
*   [ ] **4. CPU Validation:** Masuk BIOS (F1), pastikan terdeteksi **Dual Intel Xeon X5690** (Total 12 Cores / 24 Threads per server). [Intel Ark X5690](https://www.intel.com).
*   [ ] **5. Memory Validation:** Pastikan RAM terdeteksi utuh **192GB DDR3 ECC Reg** (Cek status *Healthy* di setiap slot).
*   [ ] **6. Storage Integrity:** Cek konfigurasi **RAID 1** pada SSD Enterprise. Pastikan status disk *Online & Optimal*.
*   [ ] **7. GPU Stability:** Masuk ke OS (Ubuntu), jalankan `nvidia-smi` atau `glxinfo`. Pastikan **Frame Merah Jambu (Artifact)** hilang total dan warna layar tajam.

## ⚡ III. UJI OPERASIONAL (STRESS TEST)
*   [ ] **8. Power Redundancy:** Cabut salah satu kabel Power Supply (PSU) saat server nyala. Unit **TIDAK BOLEH** mati/restart.
*   [ ] **9. Fan Speed Control:** Pastikan kipas (fans) berputar kencang saat beban berat dan melambat saat *idle* (Fungsi PWM normal).
*   [ ] **10. IMM/IPMI Access:** Pastikan modul manajemen remote (IMM) bisa diakses via web browser agar kita bisa kontrol dari Bintaro. [IBM IMM Support](https://www.ibm.com).

---

### 📝 CATATAN KHUSUS INSPEKSI:
*"Jika ada salah satu poin di atas yang GAGAL (FAIL), pembayaran tahap akhir ditunda hingga vendor melakukan perbaikan ulang sesuai Purchase Order #001."*

---
**Status Akhir:** [ LAYAK / TIDAK LAYAK ]  
**Tanda Tangan Inspektur:**  
*(Digital/Physical Signature)*  
**CAPO**
