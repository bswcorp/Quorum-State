import hashlib
import json
from datetime import datetime

class QuantumLedger:
    """
    Simulasi Buku Besar Kuantum (Quantum Ledger) untuk Quorum-State.
    Setiap blok mewakili hasil konsensus dari Quorum 676 node.
    """
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Membuat Blok Genesis (Blok Pertama)
        self.create_block(previous_hash="0" * 64, proof=100)

    def create_block(self, proof, previous_hash):
        """Membuat blok baru setelah validasi Quorum tercapai."""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
            'status': 'QUANTUM_STABLE'
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        """Menambahkan transaksi baru ke dalam antrean superposisi."""
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'security': 'Lattice-Protected'
        })
        return self.get_last_block()['index'] + 1

    @staticmethod
    def hash(block):
        """Menciptakan SHA-3 hash dari sebuah blok."""
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha3_256(encoded_block).hexdigest()

    def get_last_block(self):
        return self.chain[-1]

# Jalankan Simulasi Ledger
if __name__ == "__main__":
    q_ledger = QuantumLedger()
    
    print("[*] Menginisialisasi Quantum Ledger...")
    q_ledger.add_transaction("Genesis_Node", "BreSpeedWorks_Wallet", 5000000)
    
    print("[*] Melakukan Konsensus Quorum...")
    last_block = q_ledger.get_last_block()
    last_hash = q_ledger.hash(last_block)
    
    new_block = q_ledger.create_block(proof=451, previous_hash=last_hash)
    
    print("\n--- Blok Baru Berhasil Dicatat ---")
    print(json.dumps(new_block, indent=4))
    print(f"\nTotal Blok di Chain: {len(q_ledger.chain)}")
