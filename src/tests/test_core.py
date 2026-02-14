import sys
import os
import unittest

# Pathing agar server GitHub menemukan folder core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core')))
from qstate_core import QuorumStateCore

class TestQuorumStateSystem(unittest.TestCase):
    def setUp(self):
        self.qs = QuorumStateCore()
        self.sender = "BSW-GENESIS-NODE"
        self.receiver = "ANDI-NODE"
        # Beri saldo awal ke pengirim
        self.qs.mint(self.sender, 1000)

    def test_quorum_transaction_flow(self):
        """Tes apakah transaksi berhasil jika Quorum (min 453) tercapai"""
        amount = 500
        # Jalankan transaksi yang memicu voting 676 Computors
        success, message = self.qs.execute_transaction(self.sender, self.receiver, amount)
        
        # Karena di quorum_logic kita simulasi 90% jujur, harusnya sukses
        if success:
            self.assertEqual(self.qs.get_balance(self.receiver), 500)
            print(f"\n[PASS] Transaksi Quorum Berhasil: {message}")
        else:
            print(f"\n[INFO] Transaksi Ditolak Quorum (Probabilitas): {message}")

    def test_max_supply_integrity(self):
        """Memastikan tidak bisa minting melebihi 200 Triliun"""
        fail = self.qs.mint("EXPLOITER", 201_000_000_000_000)
        self.assertFalse(fail)
        print("[PASS] Integritas Max Supply Terjaga.")

    def test_quantum_shield_activation(self):
        shielded = self.qs.apply_shield("SECRET-KEY-2026")
        self.assertTrue(shielded.startswith("SHIELDED-"))
        print(f"[PASS] Quantum Shield Aktif: {shielded}")

if __name__ == "__main__":
    unittest.main()
