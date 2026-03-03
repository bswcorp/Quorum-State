import time
import hashlib
from datetime import datetime

class GenAtoZ_Engine:
    def __init__(self):
        self.subuh_hour = 4  # Pukul 04:00 AM (Waktu Subuh)
        self.freq_siluman = "ULTRA_SONIC_DISRUPTION"
        self.registry = {} # Database Injeksi GenAtoZ

    def inject_system(self, machine_id, commitment_score):
        """
        Remote Injection: Menentukan nasib mesin berdasarkan skor komitmen.
        """
        if commitment_score < 10:
            # Injeksi GenAtoZmad: Penyusutan Aset & Alarm Genderang
            self.registry[machine_id] = {
                "status": "GenAtoZmad",
                "payload": "ASSET_EROSION_1000T_TO_10K",
                "alarm": "GENDERANG_FREQ_SILUMAN_ACTIVE"
            }
            return f"[INJECTED] {machine_id} -> Status: GenAtoZmad (Piala Keburukan)"
        else:
            # Injeksi GenAtoZmate: Peningkatan Kapasitas & Reward
            self.registry[machine_id] = {
                "status": "GenAtoZmate",
                "payload": "QUANTUM_REWARD_BOOST",
                "alarm": "SILENT_HARMONY"
            }
            return f"[MATCHED] {machine_id} -> Status: GenAtoZmate (Piala Kebaikan)"

    def subuh_timer_check(self):
        """
        Timer Subuh: Memicu 'Bedug Subuh' secara otomatis di seluruh mesin.
        """
        now = datetime.now()
        if now.hour == self.subuh_hour:
            print(f"!!! Q-DAY SUBUH REACHED: ACTIVATING FREQ SILUMAN !!!")
            for m_id, data in self.registry.items():
                if data["status"] == "GenAtoZmad":
                    self.execute_erosion(m_id)
        else:
            print(f"Waiting for Subuh... Current Time: {now.strftime('%H:%M:%S')}")

    def execute_erosion(self, machine_id):
        # Proses penyusutan aset secara brutal sebelum matahari terbit
        print(f"[ALARM] {machine_id}: GENDERANG MEMEKIK! Aset menyusut ke Rp.0 (Bunker Gratisan).")

# Inisialisasi dari Puncak Gunung (Remote Control)
if __name__ == "__main__":
    injector = GenAtoZ_Engine()
    # Contoh Injeksi Remote ke mesin asing (Skor 5 = Rendah)
    print(injector.inject_system("MACHINE_ID_OFFSHORE", 5))
    # Contoh Injeksi ke mitra setia (Skor 10 = Pass)
    print(injector.inject_system("MACHINE_ID_PARTNER", 10))
    # Jalankan Pengecekan Timer
    injector.subuh_timer_check()
