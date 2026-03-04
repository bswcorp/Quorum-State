class QStateTaskForce:
    def __init__(self):
        self.staff_registry = {} # Data Pekerja (Finance & Marketing)
        self.zero_tolerance_active = True

    def log_operation(self, staff_id, amount, action_type):
        """
        Monitoring Kolaborasi: Finance & Marketing menyatu.
        Jika ada ketidaksesuaian data -> TENDANG (Go to Hell).
        """
        # Simulasi Verifikasi Silang (Cross-Check)
        # Jika data Marketing (Penjualan) != data Finance (Kas), PIC langsung di-slashing
        is_consistent = self.verify_data_consistency(amount)
        
        if not is_consistent:
            print(f"[CRITICAL ERROR] {staff_id}: KETIDAKJUJURAN TERDETEKSI!")
            self.terminate_staff(staff_id)
            return False
        
        print(f"[SUCCESS] Transaksi {action_type} sebesar {amount} diverifikasi.")
        return True

    def terminate_staff(self, staff_id):
        """Eksekusi Satu Kali Kesalahan: TENDANG KELUAR."""
        print(f"[TERMINATED] {staff_id}: Satu kesalahan cukup. GO TO HELL!")
        print("Mencari SDM terbarukan dari database cadangan...")
