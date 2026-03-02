import json

def kalkulator_pro_qstate():
    """
    Kalkulator Proyek Quorum-State (Barometer Anggaran).
    Konversi otomatis IDR -> USD -> $QSTATE.
    """
    print("--- 🥬 BAROMETER ANGGARAN Q-STATE (VERS. PRO) 🥬 ---")
    print("Motto: Berangkat! Zero Defect, Zero Corruption.\n")

    # 1. Konfigurasi Kurs Barometer (Bisa diupdate sesuai pasar)
    KURS_IDR_USD = 16000  # 1 USD = 16.000 IDR
    KURS_QSTATE_IDR = 250 # 1 $QSTATE = 250 IDR (Simulasi Harga Awal)

    try:
        # 2. Input Anggaran Pekerjaan
        nama_pekerjaan = input("[?] Nama Pekerjaan (misal: DCP Wilayah Timur): ") or "Survei Geoteknik"
        biaya_idr = float(input("[?] Masukkan Total Anggaran (IDR): ") or 10000000)

        # 3. Logika Konversi Barometer
        biaya_usd = biaya_idr / KURS_IDR_USD
        biaya_qstate = biaya_idr / KURS_QSTATE_IDR

        # 4. Output Barometer Multi-Currency
        print("\n" + "="*50)
        print(f"📊 LAPORAN ANGGARAN: {nama_pekerjaan.upper()}")
        print("="*50)
        print(f"🇮🇩 RUPIAH (IDR)    : Rp {biaya_idr:,.2f}")
        print(f"🇺🇸 DOLLAR (USD)    : $ {biaya_usd:,.2f}")
        print(f"🌌 Q-STATE ($QST)  : ⧫ {biaya_qstate:,.2f}")
        print("="*50)
        
        # 5. Analisis Efisiensi (Logika Tukang Sayur)
        print(f"Catatan: Barometer ini menggunakan kurs 1 $QST = Rp {KURS_QSTATE_IDR}")
        print("Status: VALID UNTUK KONTRAK / SPK.")
        print("="*50)

    except ValueError:
        print("\n[!] Masukkan angka saja, Captain! Bumbunya kebanyakan.")

if __name__ == "__main__":
    kalkulator_pro_qstate()
  
