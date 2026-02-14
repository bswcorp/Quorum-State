import sys
import os
import unittest

# Menghubungkan ke folder src/core agar file qstate_core bisa dibaca
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/core')))
from qstate_core import QuorumStateCore

class TestQuorumStateCore(unittest.TestCase):
    def setUp(self):
        """Inisialisasi setiap kali tes dijalankan"""
        self.qs = QuorumStateCore()
        self.test_address = "BSW-TEST-NODE"

    def test_minting_logic(self):
        """Memastikan pencetakan koin $QSTATE masuk ke Ledger"""
        amount = 5000
        self.qs.mint(self.test_address, amount)
        self.assertEqual(self.qs.get_balance(self.test_address), amount)
        self.assertEqual(self.qs.total_supply, amount)
        print(f"\n[PASS] Minting {amount} $QSTATE Sukses.")

    def test_quantum_shield_logic(self):
        """Memastikan fitur Shield menghasilkan hash pengaman"""
        raw_data = "SEND-100-QSTATE"
        shielded_data = self.qs.apply_shield(raw_data)
        self.assertTrue(shielded_data.startswith("SHIELDED-"))
        print(f"[PASS] Quantum Shield Berhasil Mengenkripsi Data: {shielded_data}")

    def test_contract_execution(self):
        """Memastikan kontrak hanya jalan jika saldo cukup (Logika Quorum)"""
        receiver = "RECIPIENT-ADDR"
        self.qs.mint(self.test_address, 1000)
        
        # Eksekusi sukses
        success = self.qs.execute_contract(self.test_address, receiver, 400)
        self.assertTrue(success)
        self.assertEqual(self.qs.get_balance(receiver), 400)
        
        # Eksekusi gagal (saldo tidak cukup)
        fail = self.qs.execute_contract(self.test_address, receiver, 2000)
        self.assertFalse(fail)
        print("[PASS] Smart Contract & Ledger Balance Valid.")

if __name__ == "__main__":
    unittest.main()
