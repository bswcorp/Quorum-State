class IntegrityGuard:
    def __init__(self, godfather_vision):
        self.vision = "KEJUJUURAN_DIATAS_SEGALANYA"
        self.standard_price = 100 # Sesuai Bab 30
        self.bonus_pool = "UNLIMITED_GEOF_TRAIN" # Bonus sepanjang gerbong

    def validate_sale(self, staff_id, sale_price, family_status):
        """
        Audit Transaksi: Jika sale_price > standard_price (Mark-up), 
        maka DETECTED. Jika jujur, berikan BONUS TAK TERHINGGA.
        """
        if sale_price > self.standard_price:
            print(f"[ALARM] {staff_id}: PRAKTEK CALO DETECTED! Menjual di atas harga sistem.")
            print(f"[ACTION] Memutuskan Hubungan Kerja... ENTIRE {staff_id} FROM SYSTEM.")
            return "GO_TO_HELL"
        
        # Jika jujur, sistem siapkan kesejahteraan anak-istri mereka
        print(f"[HALAL] {staff_id}: Transaksi Jujur. Bonus Sejahtera Aktif.")
        return "WELCOME_TO_PROSPERITY"
