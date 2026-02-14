import hashlib
from quorum_logic import QuorumConsensus

class QuorumStateCore:
    def __init__(self):
        self.ledger = {}
        self.MAX_SUPPLY = 200_000_000_000_000 
        self.total_supply = 0
        self.shield_active = True
        # Inisialisasi Otak Konsensus (676 Computors)
        self.consensus = QuorumConsensus(total_computors=676)

    def mint(self, address, amount):
        """Minting hanya jika dalam batas Max Supply"""
        if self.total_supply + amount <= self.MAX_SUPPLY:
            if amount > 0:
                self.ledger[address] = self.ledger.get(address, 0) + amount
                self.total_supply += amount
                return True
        return False

    def distribute_rewards(self, epoch_reward):
        """Membagikan hadiah ke 676 Computors setelah validasi"""
        if self.total_supply + epoch_reward > self.MAX_SUPPLY:
            return "[ERROR] Reward melebihi MAX_SUPPLY"

        reward_per_node = epoch_reward // self.consensus.total_computors
        for i in range(self.consensus.total_computors):
            node_address = f"COMPUTOR-{i:03d}"
            self.mint(node_address, reward_per_node)
            
        return f"[SUCCESS] {epoch_reward} $QSTATE didistribusikan via Quorum."

    def execute_transaction(self, sender, receiver, amount):
        """
        Menjalankan transaksi HANYA jika disetujui oleh minimal 453 Computors.
        """
        tx_id = hashlib.sha256(f"{sender}{receiver}{amount}".encode()).hexdigest()
        
        # 1. Kumpulkan suara dari Quorum
        self.consensus.collect_votes(tx_id)
        
        # 2. Verifikasi apakah Quorum tercapai (Min 453 Yes)
        is_valid, message = self.consensus.verify_quorum(tx_id)
        
        if is_valid and self.get_balance(sender) >= amount:
            self.ledger[sender] -= amount
            self.ledger[receiver] = self.ledger.get(receiver, 0) + amount
            return True, f"TX Valid: {message}"
        else:
            return False, f"TX Rejected: {message}"

    def get_balance(self, address):
        return self.ledger.get(address, 0)

    def apply_shield(self, transaction_data):
        if self.shield_active:
            shield_hash = hashlib.sha3_256(f"QS-{transaction_data}".encode()).hexdigest()
            return f"SHIELDED-{shield_hash[:16]}"
        return transaction_data
