import time
from datetime import datetime

class RoyalPayroll:
    def __init__(self):
        self.standard_salary = 100_000_000 # Gaji Pokok Mewah (Contoh: 100jt)
        self.bonus_per_honesty = 50_000_000 # Bonus Kejujuran (Deretan Nol)
        self.records = {}

    def generate_slip(self, staff_id, name, position, conduct_score):
        """
        Mencetak Slip Gaji Otomatis:
        - Jika Skor 100: Gaji + Bonus Tak Terhingga.
        - Jika Skor < 100: Peringatan Merah.
        - Jika Skor 0 (Korupsi): ENTIRE / KICK.
        """
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
        total_salary = self.standard_salary
        status = "ABDI DALAM (SETIA)"
        color_code = "BLUE_INK"

        if conduct_score >= 100:
            total_salary += self.bonus_per_honesty
            note = "KEBAIKAN TERPUJI: BONUS GERBONG KERETA AKTIF."
        elif conduct_score == 0:
            return f"!!! CRITICAL: {name} (ID: {staff_id}) TELAH DI-ENTIRE. TIDAK LAYAK MENERIMA HAK. !!!"
        else:
            status = "DALAM PENGAWASAN"
            note = "PERINGATAN: ADA KESALAHAN TERCATAT."
            color_code = "RED_INK"

        # Format Slip untuk Mesin Printer Tangguh
        slip = f"""
        ========================================
        🏛️ QSTATE ROYAL PAYROLL - GENERATION 5.0
        ========================================
        TANGGAL  : {timestamp}
        ID STAF  : {staff_id}
        NAMA     : {name}
        JABATAN  : KEPALA DIVISI ({position})
        STATUS   : {status}
        ----------------------------------------
        GAJI POKOK  : Rp {total_salary:,}
        BONUS HALAL : Rp {(total_salary - self.standard_salary):,}
        ----------------------------------------
        CATATAN: {note}
        INK COLOR: {color_code}
        ========================================
        VISI: ANDI MUHAMMAD HARPIANTO
        """
        return slip

# Simulasi Pencetakan
if __name__ == "__main__":
    payroll = RoyalPayroll()
    # Contoh Abdi Dalam yang Jujur
    print(payroll.generate_slip("DIV-FIN-001", "Ksatria Jujur", "Finance", 100))
