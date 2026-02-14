import sys
import os
import unittest

# Pathing agar server GitHub tidak nyasar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core')))
from qstate_core import QuorumStateCore

class TestQuorumStateCore(unittest.TestCase):
    def setUp(self):
        self.qs = QuorumStateCore()
        self.test_address = "BSW-TEST-NODE"

    def test_minting_and_supply(self):
        """Tes batas MAX_SUPPLY 200 Triliun"""
        # Minting dalam batas
        success = self.qs.mint(self.test_address, 1000)
        self.assertTrue(success)
        self.assertEqual(self.qs.get_balance(self.test_address), 1000)
        
        # Percobaan minting melebihi MAX_SUPPLY
        fail = self.qs.mint("SCAMMER", 201_000_000_000_000)
        self.assertFalse(fail)

    def test_distribute_rewards(self):
        """Tes distribusi ke 676 Computors"""
        reward_pool = 1000000
        msg = self.qs.distribute_rewards(reward_pool)
        self.assertIn("[SUCCESS]", msg)
        # Cek saldo salah satu node (node ke-100)
        balance = self.qs.get_balance("COMPUTOR-100")
        self.assertEqual(balance, reward_pool // 676)

    def test_quantum_shield(self):
        shielded = self.qs.apply_shield("SECURE-DATA")
        self.assertTrue(shielded.startswith("SHIELDED-"))

if __name__ == "__main__":
    unittest.main()
