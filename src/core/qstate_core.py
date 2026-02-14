import hashlib
import time

class QuorumStateCore:
    def __init__(self):
        self.ledger = {}
        # Menetapkan MAX_SUPPLY: 200 Triliun koin (sesuai visi Qubic)
        self.MAX_SUPPLY = 200_000_000_000_000 
        self.total_supply = 0
        self.shield_active = True
        self.computors_count = 676  # Jumlah node validator utama

    def mint(self, address, amount):
        """Fungsi Minting dengan pengecekan batas maksimal suplai"""
        if self.total_supply + amount <= self.MAX_SUPPLY:
            if amount > 0:
                self.ledger[address] = self.ledger.get(address, 0) + amount
                self.total_supply += amount
                return True
        return False

    def distribute_rewards(self, epoch_reward):
        """
        Membagikan hadiah koin ke 676 Computors (Validator).
        Ini mensimulasikan sistem distribusi emisi mingguan.
        """
        if self.total_supply + epoch_reward > self.MAX_SUPPLY:
            return "[ERROR] Reward melebihi MAX_SUPPLY"

        reward_per_node = epoch_reward // self.computors_count
        
        # Simulasi pembagian ke semua node (kita gunakan loop sederhana)
        for i in range(self.computors_count):
            node_address = f"COMPUTOR-{i:03d}"
            self.mint(node_address, reward_per_node)
            
        return f"[SUCCESS] {epoch_reward} $QSTATE didistribusikan ke {self.computors_count} node."

    def get_balance(self, address):
        return self.ledger.get(address, 0)

    def apply_shield(self, transaction_data):
        if self.shield_active:
            shield_hash = hashlib.sha3_256(f"QS-{transaction_data}".encode()).hexdigest()
            return f"SHIELDED-{shield_hash[:16]}"
        return transaction_data

    def execute_contract(self, sender, receiver, amount, condition_met=True):
        if condition_met and self.get_balance(sender) >= amount:
            self.ledger[sender] -= amount
            self.ledger[receiver] = self.ledger.get(receiver, 0) + amount
            return True
        return False
