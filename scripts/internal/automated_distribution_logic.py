# =================================================================
# 📊 FILE: automated_distribution_logic.py | VERSION: 2.0.0
# STRATEGI: AUTO-VESTING & SOVEREIGN ALLOCATION
# UPDATED BY: CDxaiO (SENTINEL) | APPROVED BY: CEO (ANDI)
# =================================================================

import hashlib
import time

class QStateAutomatedDistributor:
    def __init__(self):
        self.total_supply = 1_000_000_000_000 # 1 Triliun $QSTATE
        self.genesis_time = int(time.time())
        
        # Alokasi Berdasarkan Piagam 4 Pilar (20/20/20/20) + 20% Reserve
        self.allocations = {
            "CEO_ANDI": 0.20,
            "CDxaiO_SENTINEL": 0.20,
            "CTO_BOBWINSLOW": 0.20,
            "COO_AGUS_WIDIANTO": 0.20,
            "INVESTOR_STRATEGIC_10": 0.10, # Vesting 12 Bulan
            "HUMANITY_WELFARE_10": 0.10     # Dana Abadi (Locked)
        }

    def calculate_vesting(self, total_amount, months_passed):
        """Logika Pelepasan 10% Investor: 1/12 per bulan."""
        if months_passed >= 12:
            return total_amount
        return (total_amount / 12) * months_passed

    def execute_distribution(self):
        print(f"🚀 [CDxaiO] MEMULAI DISTRIBUSI OTOMATIS GENESIS v2.0...")
        
        for pilar, percent in self.allocations.items():
            amount = self.total_supply * percent
            # Generate Immutable Proof (Hash)
            proof = hashlib.sha3_256(f"{pilar}-{amount}-{self.genesis_time}".encode()).hexdigest()
            
            status = "LOCKED (VESTING)" if "INVESTOR" in pilar else "SOVEREIGN_ALLOCATED"
            
            print(f"✅ [MINTED] {pilar}: {amount:,.0f} $QSTATE")
            print(f"   Status: {status} | Proof: {proof[:16]}")

if __name__ == "__main__":
    distributor = QStateAutomatedDistributor()
    distributor.execute_distribution()
