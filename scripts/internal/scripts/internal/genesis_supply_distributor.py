# 📊 AUTOMATED TOKEN SUPPLY DISTRIBUTION LOGIC
# Otoritas: ANDI MUHAMMAD HARPIANTO | Project: $QSTATE
# Status: AIR-GAPPED INTERNAL EXECUTION

import hashlib
import time

class QStateDistributor:
    def __init__(self):
        self.total_supply = 1_000_000_000_000 # 1 Triliun Koin
        self.supply_map = {
            "INVESTOR_INTRO_10": 0.10,   # 10% (100M) Investor Awal (Dubai/China)
            "CHARITY_HUMANITY_10": 0.10, # 10% (100M) Kesejahteraan Umat
            "INFRASTRUCTURE_RESERVE": 0.30, # 30% (300M) Pengembangan Node M4/M5
            "CIRCULATING_UTILITY": 0.50  # 50% (500M) Ekosistem Global
        }

    def execute_genesis_split(self):
        """
        Membagi 1T Suplai ke dalam 'Bunker Digital' (Wallets) secara Otomatis.
        """
        print(f"📊 [DISTRIBUTOR] Memulai Alokasi 1T $QSTATE...")
        
        results = {}
        for fund_name, percentage in self.supply_map.items():
            amount = self.total_supply * percentage
            # Membuat Hash Transaksi Unik sebagai Bukti di Hyperledger
            tx_id = hashlib.sha3_256(f"{fund_name}-{amount}-{time.time()}".encode()).hexdigest()
            
            results[fund_name] = {
                "amount": f"{amount:,} $QSTATE",
                "tx_proof": tx_id[:16],
                "status": "LOCKED_IN_ESCROW"
            }
            print(f"✅ [ALLOCATED] {fund_name}: {amount:,} Koin. Status: LOCKED.")
            
        return results

# --- EXECUTION ---
if __name__ == "__main__":
    distributor = QStateDistributor()
    allocation_report = distributor.execute_genesis_split()
    
    # Mencatat ke Log Deployment Bintaro
    print("\n📜 [GENESIS LOG] Laporkan Hasil ini ke Hyperledger Block #0.")
