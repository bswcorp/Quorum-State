# 🛡️ SENTINEL AI: SOVEREIGN MONITORING SYSTEM
# Otoritas: ANDI MUHAMMAD HARPIANTO | Node: 01 BINTARO
# Status: AUTOMATED DEFENSE ACTIVE

import os
import time
import hashlib

class SentinelAI:
    def __init__(self):
        self.target_files = ["MASTER_EXECUTIVE_SUMMARY.md", "scripts/internal/stellar_kernel_ops.py"]
        self.file_hashes = self._capture_fingerprints()
        self.security_status = "STABLE"

    def _capture_fingerprints(self):
        """Mengunci sidik jari digital (Hash) kode asli."""
        hashes = {}
        for f in self.target_files:
            if os.path.exists(f):
                content = open(f, 'rb').read()
                hashes[f] = hashlib.sha3_256(content).hexdigest()
        return hashes

    def pulse_check(self):
        """Memantau integritas file dan upaya penyusupan."""
        while True:
            print("👁️ [SENTINEL] Memindai Integritas Bunker...")
            
            # 1. Cek Perubahan Kode (Anti-Tamper)
            for f, original_hash in self.file_hashes.items():
                current_content = open(f, 'rb').read()
                current_hash = hashlib.sha3_256(current_content).hexdigest()
                
                if current_hash != original_hash:
                    self._trigger_sovereign_veto(f"TAMPER_DETECTED: {f}")

            # 2. Cek Koneksi Luar (Anti-Spying)
            # Jika kabel internet dicolok paksa, Sentinel akan mendeteksi IP.
            if os.system("ping -c 1 8.8.8.8 > /dev/null 2>&1") == 0:
                self._trigger_sovereign_veto("UNAUTHORIZED_INTERNET_CONNECTION")

            time.sleep(60) # Scan setiap 60 detik

    def _trigger_sovereign_veto(self, reason):
        print(f"🚨 [CRITICAL] {reason}!")
        print("☢️ [VETO] MENGHANCURKAN AKSES... ISOLASI TOTAL!")
        # Panggil script veto yang sudah kita buat
        os.system("python3 scripts/internal/sovereign_veto.py")
        exit()

if __name__ == "__main__":
    sentinel = SentinelAI()
    sentinel.pulse_check()
