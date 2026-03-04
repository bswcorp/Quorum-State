class QStateDistributor:
    def __init__(self, master_supply=100_000_000_000): # 100M (10% dari 1T)
        self.marketing_vault = 0
        self.current_price = 100 # Rupiah
        self.step_size = 10_000_000 # 1% (10M koin)
        self.stage = 1

    def release_to_coo(self):
        """Melepaskan 1% koin ke dompet Marketing hanya jika tahap sebelumnya selesai"""
        if self.marketing_vault == 0:
            self.marketing_vault = self.step_size
            print(f"[RELEASE] Tahap {self.stage}: 10M Koin dilepas ke COO.")
            print(f"[PRICE CONTROL] Harga ditetapkan: Rp.{self.current_price}")
            
            # Persiapan untuk tahap berikutnya
            self.current_price += 100 
            self.stage += 1
        else:
            print("[DENIED] Dompet Marketing masih memiliki stok. Selesaikan penjualan!")

# Inisialisasi Kontrol
distributor = QStateDistributor()
distributor.release_to_coo()
