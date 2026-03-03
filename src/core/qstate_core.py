import hashlib
import time
from datetime import datetime
from quorum_logic import QuorumConsensus

class QuorumStateCore:
    def __init__(self):
        self.ledger = {}
        self.MAX_SUPPLY = 200_000_000_000_000 
        self.total_supply = 0
        self.shield_active = True
        self.consensus = QuorumConsensus(total_computors=676)
        
        # --- INTEGRASI MODUL INJEKSI GENATOZ ---
        self.gen_registry = {} # Database Status GenAtoZmad/Mate
        self.subuh_hour = 4    # Jam eksekusi 'Bedug Subuh' (04:00 AM)

    def apply_gen_ato_z(self, address, commitment_score):
        """
        Injeksi Remote: Menentukan nasib aset berdasarkan skor Kuda-Kuda.
        """
        if commitment_score < 10:
            self.gen_registry[address] = "GenAtoZmad" # Piala Keburukan
            return f"[INJECTED] {address} -> Status: GenAtoZmad (Alarm Aktif!)"
        else:
            self.gen_registry[address] = "GenAtoZmate" # Piala Kebaikan
            return f"[MATCHED] {address} -> Status: GenAtoZmate (Safe Passage)"

    def execute_transaction(self, sender, receiver, amount, sender_score=10):
        """
        Transaksi dengan Filter Kuda-Kuda & Timer Subuh.
        """
        # 1. Cek Status Injeksi (GenAtoZ Check)
        status = self.apply_gen_ato_z(sender, sender_score)
        
        # 2. Logika 'Bedug Subuh' (Penyusutan Otomatis)
        now = datetime.now()
        if now.hour == self.subuh_hour and self.gen_registry.get(sender) == "GenAtoZmad":
            self.ledger[sender] = 0 # Erosi Aset ke Rp.0 (Bunker Gratisan)
            return False, f"CRITICAL: {sender} terkena Erosi Subuh! Aset Musnah."

        # 3. Jalankan Konsensus Quorum Biasa
        tx_id = hashlib.sha256(f"{sender}{receiver}{amount}".encode()).hexdigest()
        self.consensus.collect_votes(tx_id)
        is_valid, message = self.consensus.verify_quorum(tx_id)
        
        if is_valid and self.get_balance(sender) >= amount:
            self.ledger[sender] -= amount
            self.ledger[receiver] = self.ledger.get(receiver, 0) + amount
            return True, f"Success: {status} | {message}"
        
        return False, f"Rejected: {status} | {message}"

    def get_balance(self, address):
        return self.ledger.get(address, 0)

    def mint(self, address, amount):
        if self.total_supply + amount <= self.MAX_SUPPLY:
            self.ledger[address] = self.ledger.get(address, 0) + amount
            self.total_supply += amount
            return True
        return False
