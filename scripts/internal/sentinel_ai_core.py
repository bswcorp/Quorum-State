# 👁️ SENTINEL AI: AUTOMATED SOVEREIGN MONITORING
# Otoritas: ANDI MUHAMMAD HARPIANTO | Node: 01 BINTARO
# Status: ACTIVE WATCHDOG

import os, time, hashlib, subprocess

class SentinelSentinel:
    def __init__(self):
        self.fingerprints = self._lock_base_hashes()
        self.lockdown_status = False

    def _lock_base_hashes(self):
        """Mengunci tanda tangan digital file sensitif."""
        files = ["MASTER_EXECUTIVE_SUMMARY.md", "scripts/internal/stellar_kernel_ops.py"]
        return {f: hashlib.sha3_256(open(f, 'rb').read()).hexdigest() for f in files if os.path.exists(f)}

    def scan_environment(self):
        """Pemindaian 360 derajat: Fisik, Jaringan, dan Integritas File."""
        while not self.lockdown_status:
            # 1. Cek Integritas File (Anti-Tamper)
            for f, original in self.fingerprints.items():
                current = hashlib.sha3_256(open(f, 'rb').read()).hexdigest()
                if current != original:
                    self._execute_emergency_veto(f"KODE BERUBAH PADA: {f}")

            # 2. Cek Koneksi Luar (Anti-Spying/Leak)
            # Sentinel mendeteksi jika kabel WAN dicolok paksa
            if self._check_external_ping():
                self._execute_emergency_veto("DETEKSI KONEKSI INTERNET ILEGAL")

            time.sleep(30) # Scan setiap 30 detik

    def _check_external_ping(self):
        return os.system("ping -c 1 8.8.8.8 > /dev/null 2>&1") == 0

    def _execute_emergency_veto(self, reason):
        print(f"🚨 [SENTINEL ALERT] {reason}!")
        self.lockdown_status = True
        # Menjalankan hulu ledak penghapusan akses
        subprocess.call(["python3", "scripts/internal/sovereign_veto.py"])

if __name__ == "__main__":
    sentinel = SentinelSentinel()
    sentinel.scan_environment()
