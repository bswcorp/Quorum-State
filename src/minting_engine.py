import hashlib
import time
import random

class QStateMinting:
    """
    Simulasi Minting $QSTATE melalui Useful Proof of Work (UPoW).
    Koin dihasilkan dari penyelesaian tugas pelatihan AI.
    """
    def __init__(self, reward_per_block=1000):
        self.reward = reward_per_block
        self.difficulty = 4  # Simulasi tingkat kesulitan

    def train_ai_model(self, task_data):
        """Simulasi penambang yang melatih jaringan saraf AI."""
        print(f"[*] Memulai Pelatihan AI: {task_data}")
        nonce = 0
        start_time = time.time()
        
        while True:
            # Hash merepresentasikan 'hasil kerja' komputasi AI
            check = hashlib.sha3_256(f"{task_data}{nonce}".encode()).hexdigest()
            if check.startswith("0" * self.difficulty):
                duration = time.time() - start_time
                return nonce, check, duration
            nonce += 1

    def issue_reward(self, wallet_address):
        """Memberikan koin $QSTATE kepada penambang."""
        print(f"[✔] Blok Valid! Mengirim {self.reward} $QSTATE ke {wallet_address}")

if __name__ == "__main__":
    miner_wallet = "BreSpeedWorks_Quantum_Wallet"
    engine = QStateMinting()
    
    # Tugas AI: Mensimulasikan deteksi pola dalam data kuantum
    task = "Quantum_Pattern_Recognition_Task_#001"
    
    nonce, result_hash, time_taken = engine.train_ai_model(task)
    
    print(f"\nHasil Kerja (UPoW):")
    print(f"- Nonce: {nonce}")
    print(f"- Hash: {result_hash}")
    print(f"- Waktu: {time_taken:.2f} detik")
    
    engine.issue_reward(miner_wallet)
