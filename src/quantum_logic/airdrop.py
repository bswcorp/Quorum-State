class QStateAirdrop:
    """
    Simulasi Mekanisme Airdrop untuk menarik 10.000 pemegang koin pertama.
    Setiap partisipan baru akan mendapatkan 10.000 $QSTATE secara gratis.
    """
    def __init__(self):
        self.airdrop_reward = 10000
        self.total_distributed = 0
        self.participants = set()

    def claim_airdrop(self, wallet_address):
        if wallet_address in self.participants:
            return f"Error: Wallet {wallet_address} sudah melakukan klaim!"
        
        # Simulasi verifikasi kuantum sebelum klaim
        print(f"[*] Melakukan Verifikasi Kuantum untuk: {wallet_address}...")
        self.participants.add(wallet_address)
        self.total_distributed += self.airdrop_reward
        
        return f"Sukses! 10.000 $QSTATE telah dikirim ke {wallet_address}. Total Distribusi: {self.total_distributed}"

if __name__ == "__main__":
    airdrop_system = QStateAirdrop()
    
    # Simulasi klaim dari komunitas awal
    print(airdrop_system.claim_airdrop("User_001_BreSpeedWorks"))
    print(airdrop_system.claim_airdrop("User_002_QuantumFan"))
    # Coba klaim ulang
    print(airdrop_system.claim_airdrop("User_001_BreSpeedWorks"))
