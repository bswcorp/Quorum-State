import time
from core.qstate_core import QuorumStateCore

def start_node():
    print("=== QUORUM-STATE ($QSTATE) NODE INITIALIZATION ===")
    print("Connecting to 676 Computors... [OK]")
    print("Activating Quantum Shield... [OK]")
    
    # Inisialisasi Mesin Utama
    q_state = QuorumStateCore()
    
    # Simulasi Siklus Hidup Jaringan
    try:
        print("\n--- Jaringan Berjalan (Listening for Transactions) ---")
        # Contoh Minting Genesis
        q_state.mint("BSW-GENESIS-NODE", 1000000)
        print(f"Genesis Balance: {q_state.get_balance('BSW-GENESIS-NODE')} $QSTATE")
        
        while True:
            # Simulasi Pemrosesan Blok tiap 10 detik (Epoch)
            print(f"\n[INFO] Time: {time.ctime()}")
            print(f"Current Supply: {q_state.total_supply} / {q_state.MAX_SUPPLY}")
            
            # Simulasi Distribusi Hadiah ke Computors
            status = q_state.distribute_rewards(100000) # 100k per epoch
            print(status)
            
            time.sleep(10) # Jeda waktu epoch
            
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Kapal berlabuh, sistem dimatikan secara aman.")

if __name__ == "__main__":
    start_node()
