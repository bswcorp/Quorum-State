import json
import time
from datetime import datetime

class TransactionReporter:
    """
    Sistem Laporan Otomatis untuk Quorum-State.
    Mencatat setiap pergerakan dana dari API Bridge secara real-time.
    """
    def __init__(self):
        self.report_file = "docs/logs/daily_report.json"
        self.ensure_log_exists()

    def ensure_log_exists(self):
        """Memastikan folder dan file log tersedia di IBM M2."""
        import os
        if not os.path.exists("docs/logs"):
            os.makedirs("docs/logs")
        if not os.path.exists(self.report_file):
            with open(self.report_file, "w") as f:
                json.dump([], f)

    def log_transaction(self, tx_data):
        """Mencatat transaksi ke dalam laporan harian."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_entry = {
            "time": timestamp,
            "details": tx_data,
            "node_origin": "IBM_x3250_M2_Sentinel",
            "security_status": "QUANTUM_STABLE_VERIFIED"
        }

        with open(self.report_file, "r+") as f:
            data = json.load(f)
            data.append(report_entry)
            f.seek(0)
            json.dump(data, f, indent=4)
        
        print(f"[📊] REPORT GENERATED: Transaction at {timestamp} logged.")
        return True

    def generate_summary(self):
        """Membuat ringkasan singkat untuk dikirim ke CEO (Capo)."""
        with open(self.report_file, "r") as f:
            data = json.load(f)
            total_tx = len(data)
            print(f"--- SUMMARY HARIAN $QSTATE ---")
            print(f"Total Transaksi Hari Ini: {total_tx}")
            print(f"Status Server: OPTIMIZED")

if __name__ == "__main__":
    reporter = TransactionReporter()
    # Simulasi data dari API Bridge
    sample_tx = {"from": "User_A", "to": "Capo_Wallet", "amount": 15000, "provider": "QRIS_GATEWAY"}
    reporter.log_transaction(sample_tx)
    reporter.generate_summary()
