import hashlib
from datetime import datetime

class QuorumStateCore:
    def __init__(self):
        # Inisialisasi Ledger dengan Bunker Rakyat
        self.ledger = {"BUNKER-RAKYAT-MISKIN": 0} 
        self.MAX_SUPPLY = 200_000_000_000_000 
        self.total_supply = 0
        self.shield_active = True
        self.packman_ratio = 0.20 # 20% Keuntungan sistem dimuntahkan ke rakyat

    def mint(self, address, amount):
        if self.total_supply + amount <= self.MAX_SUPPLY:
            self.ledger[address] = self.ledger.get(address, 0) + amount
            self.total_supply += amount
            return True
        return False

    def activate_packman(self, profit_amount):
        """
        Strategi Packman: Menghisap keuntungan dari transaksi raksasa
        dan memuntahkannya ke Bunker Rakyat Miskin (Sesuai Bab 15).
        """
        to_bunker = profit_amount * self.packman_ratio
        self.mint("BUNKER-RAKYAT-MISKIN", to_bunker)
        return to_bunker

    def get_balance(self, address):
        return self.ledger.get(address, 0)

    def apply_shield(self, data):
        if self.shield_active:
            shield_hash = hashlib.sha256(data.encode()).hexdigest()
            return f"SHIELDED-{shield_hash[:16]}"
        return data
