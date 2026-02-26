import hashlib
import time

class QWallet:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.balance = 0.0

    def sync_with_hyperledger(self, ledger_balance):
        """Menyamakan saldo dompet dengan Buku Besar IBM."""
        self.balance = ledger_balance
        print(f"🔄 [SYNC] Dompet {self.owner} Terkoneksi. Saldo: {self.balance} $QSTATE")

    def transfer(self, recipient, amount, bio_auth_key):
        """Protokol Pengiriman: Membutuhkan Kunci Biologi."""
        if bio_auth_key == "MASTER_BIO_KEY_ANDI": # Simulasi H2K
            if self.balance >= amount:
                self.balance -= amount
                tx_id = hashlib.sha256(f"{self.owner}{recipient}{amount}{time.time()}".encode()).hexdigest()
                print(f"🚀 [SEND] Mengirim {amount} ke {recipient}...")
                print(f"💎 [TX-ID] {tx_id}")
                return True
            else:
                print("❌ [FAILED] Saldo Tidak Cukup!")
        else:
            print("⚠️ [ALERT] Biometrik Salah! Akses Diblokir.")
        return False

# --- EKSEKUSI DI BINTARO ---
if __name__ == "__main__":
    my_wallet = QWallet("ANDI MUHAMMAD HARPIANTO")
    my_wallet.sync_with_hyperledger(1000000000000.0) # 1T Genesis
    my_wallet.transfer("INVESTOR_DUBAI_10%", 100000000000.0, "MASTER_BIO_KEY_ANDI")
