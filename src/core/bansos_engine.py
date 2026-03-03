import time
from datetime import datetime

class BansosEngine:
    def __init__(self, core_system):
        self.core = core_system
        self.recipients = {} # Database Rakyat Miskin Terverifikasi (Eye-ID)
        self.bunker_address = "BUNKER-RAKYAT-MISKIN"

    def register_recipient(self, address, eye_id_hash):
        """Mendaftarkan rakyat yang berhak menerima bansos via Eye-ID"""
        self.recipients[address] = {
            "eye_id": eye_id_hash,
            "last_claim": None,
            "status": "VERIFIED"
        }
        return f"[REGISTRASI] Alamat {address} resmi masuk daftar penerima manfaat."

    def distribute_aid(self, amount_per_person):
        """
        Distribusi Massal: Memuntahkan isi Bunker ke semua penerima.
        Dijalankan otomatis oleh sistem setiap periode tertentu.
        """
        total_recipients = len(self.recipients)
        total_needed = amount_per_person * total_recipients
        
        # Cek apakah saldo Bunker mencukupi
        bunker_balance = self.core.get_balance(self.bunker_address)
        
        if bunker_balance >= total_needed:
            print(f"--- MEMULAI DISTRIBUSI BANSOS: {total_needed} $QSTATE ---")
            for address in self.recipients:
                # Verifikasi Kelayakan (Contoh: sebulan sekali)
                self.core.mint(address, amount_per_person)
                # Kurangi saldo Bunker
                self.core.ledger[self.bunker_address] -= amount_per_person
                print(f"[SENT] {amount_per_person} $QSTATE dikirim ke {address} (Tanpa Potongan)")
            return True
        else:
            print("[ALERT] Saldo Bunker Rakyat tidak cukup! Segera aktifkan Packman.")
            return False

    def trigger_emergency_aid(self, address, eye_id_verify):
        """Bantuan Darurat: Cair seketika jika Eye-ID cocok"""
        if address in self.recipients and self.recipients[address]["eye_id"] == eye_id_verify:
            amount = 1000 # Jumlah bantuan darurat
            if self.core.mint(address, amount):
                return True, f"Bantuan Darurat Cair ke {address}."
        return False, "Verifikasi Gagal."
