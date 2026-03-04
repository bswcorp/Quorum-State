import datetime

class QStateReporting:
    def __init__(self):
        self.project_name = "QUORUM-STATE ($QSTATE)"
        self.godfather = "ANDI MUHAMMAD HARPIANTO"

    def generate_header(self, report_type):
        now = datetime.datetime.now().strftime("%B %Y")
        header = f"""
        ==================================================
        🏛️ {self.project_name} - {report_type}
        PERIOD: {now} | BY ORDER OF THE GODFATHER
        ==================================================
        STATUS: SECURE | ALIAS: GHOST PROTOCOL
        --------------------------------------------------
        """
        return header

    def create_initial_report(self):
        # Data untuk RI-01 dan Dirjen
        content = """
        [1] INFRASTRUKTUR: LENOVO & XIAOMI H2K READY.
        [2] ASSET: 100,000,000,000 $QSTATE (DECLARED).
        [3] STATUS: WAJIB LAPOR (REHABILITASI AKTIF).
        [4] TARGET: HAPUS TIRANI & BIROKRASI BOTOL.
        """
        return self.generate_header("INITIAL GENESIS REPORT") + content

# Inisialisasi Laporan
if __name__ == "__main__":
    rep = QStateReporting()
    print(rep.create_initial_report())
