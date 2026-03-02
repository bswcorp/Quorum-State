import json

def kalkulator_tukang_sayur_dcp():
    """
    Kalkulator Biaya Survei DCP (Geoteknik) - Versi Quorum-State.
    Hitungan cepat, jujur, dan terukur.
    """
    print("--- 🥬 KALKULATOR TUKANG SAYUR DCP (Q-STATE) 🥬 ---")
    print("Motto: Hitung Cepat, Kerja Tepat, Hasil Selamat (Zero Defect).\n")

    # 1. Input Data Dasar
    try:
        biaya_per_titik = float(input("[?] Harga survei per titik DCP (IDR): ") or 500000)
        jumlah_titik = int(input("[?] Berapa titik per wilayah (Barat/Tengah/Timur): ") or 50)
        biaya_mobilisasi = float(input("[?] Biaya kirim armada/alat berat (IDR): ") or 5000000)
        uang_makan_tim = float(input("[?] Jatah bumbu & kopi tim lapangan (IDR/hari): ") or 200000)
        durasi_hari = int(input("[?] Estimasi berapa hari kerja: ") or 7)

        # 2. Rumus Hitung Cepat (Logika Tukang Sayur)
        subtotal_dcp = biaya_per_titik * jumlah_titik
        total_uang_makan = uang_makan_tim * durasi_hari
        biaya_admin_arsip = subtotal_dcp * 0.05 # Biaya kertas & pulpen 5%
        
        total_biaya = subtotal_dcp + biaya_mobilisasi + total_uang_makan + biaya_admin_arsip

        # 3. Output Hasil
        print("\n" + "="*40)
        print(f"💰 TOTAL ANGGARAN PER WILAYAH: Rp {total_biaya:,.2f}")
        print("="*40)
        print(f"  - Biaya Jasa DCP: Rp {subtotal_dcp:,.2f}")
        print(f"  - Logistik Alat:  Rp {biaya_mobilisasi:,.2f}")
        print(f"  - Bumbu & Kopi:   Rp {total_uang_makan:,.2f}")
        print(f"  - Administrasi:   Rp {biaya_admin_arsip:,.2f}")
        print("="*40)
        print("Status: AMAN UNTUK SPK. Berangkat! 🚀")

    except ValueError:
        print("\n[!] Masukkan angka saja, Captain! Jangan campur bumbu dulu.")

if __name__ == "__main__":
    kalkulator_tukang_sayur_dcp()
