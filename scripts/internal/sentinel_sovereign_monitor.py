# 👁️ SENTINEL AI: SOVEREIGN MONITORING SYSTEM
# Otoritas: ANDI MUHAMMAD HARPIANTO | Node: 01 BINTARO
# Status: AUTOMATED DEFENSE ACTIVE (CDxaiO v2.0.0)

import os, time, hashlib, subprocess

class SentinelAI:
    def __init__(self):
        # Target yang dipantau (Konfigurasi & Kernel Utama)
        self.critical_assets = [
            "MASTER_EXECUTIVE_SUMMARY.md", 
            "scripts/internal/automated_distribution_logic.py"
        ]
        self.fingerprints = self._lock_fingerprints()

    def _lock_fingerprints(self):
        """Mengunci sidik jari digital (SHA-3) file saat startup."""
        hashes = {}
        for f in self.critical_assets:
            if os.path.exists(f):
                content = open(f, 'rb').read()
                hashes[f] = hashlib.sha3_256(content).hexdigest()
        return hashes

    def pulse_check(self):
        """Scanning berkelanjutan tanpa henti (Looping v2.0)."""
        while True:
            # 1. Integrity Check (Anti-Tamper)
            for f, original_hash in self.fingerprints.items():
                current_hash = hashlib.sha3_256(open(f, 'rb').read()).hexdigest()
                if current_hash != original_hash:
                    self._trigger_sovereign_veto(f"TAMPER DETECTED: {f}")

            # 2. Network Check (Anti-Spying/Leak)
            # Jika terdeteksi koneksi luar di lingkungan Air-Gap
            if os.system("ping -c 1 8.8.8.8 > /dev/null 2>&1") == 0:
                self._trigger_sovereign_veto("UNAUTHORIZED_EXTERNAL_NETWORK")

            time.sleep(30) # Interval scan 30 detik

    def _trigger_sovereign_veto(self, reason):
        print(f"🚨 [SENTINEL ALERT] {reason}!")
        # Jalankan protokol Veto untuk memusnahkan akses/data sensitif
        subprocess.call(["python3", "scripts/internal/sovereign_veto.py"])
        exit()

if __name__ == "__main__":
    sentinel = SentinelAI()
    sentinel.pulse_check()
