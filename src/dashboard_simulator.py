import time
import random
import os

# Konfigurasi Quorum-State
TOTAL_NODES = 676
REQUIRED_QUORUM = 451 # 2/3 mayoritas

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_dashboard(nodes, epoch, tx_id, confirmed_count):
    clear_screen()
    print("=" * 60)
    print(f" QUORUM-STATE ($QSTATE) - QUANTUM CONSENSUS DASHBOARD")
    print("=" * 60)
    print(f" Transaction ID : {tx_id}")
    print(f" Current Epoch  : {epoch}")
    print(f" Active Nodes   : {TOTAL_NODES} Computors")
    print(f" Status         : {'[ COLLAPSING ]' if confirmed_count < REQUIRED_QUORUM else '[ FINALIZED ]'}")
    print("-" * 60)
    
    # Menampilkan grid node (simulasi visual)
    # . = standby, # = validating, Q = quantum verified
    grid_view = ""
    for i, status in enumerate(nodes[:200]): # Tampilkan 200 node saja agar muat di layar
        if i % 20 == 0: grid_view += "\n"
        grid_view += f" {status} "
    
    print(grid_view)
    print("\n" + "-" * 60)
    print(f" Quorum Progress: [{confirmed_count}/{REQUIRED_QUORUM}] Nodes Confirmed")
    print("=" * 60)

def run_simulation():
    tx_id = "QS-TX-999-SUPERPOSITION"
    nodes = ["."] * TOTAL_NODES
    confirmed_count = 0
    epoch = 1
    
    while confirmed_count < REQUIRED_QUORUM:
        # Simulasi node yang mulai memvalidasi (Status Quantum)
        new_validations = random.randint(10, 40)
        for _ in range(new_validations):
            idx = random.randint(0, TOTAL_NODES - 1)
            if nodes[idx] == ".":
                nodes[idx] = "Q" # Node mencapai status Quantum-Verified
                confirmed_count += 1
        
        draw_dashboard(nodes, epoch, tx_id, confirmed_count)
        epoch += 1
        time.sleep(0.3) # Kecepatan simulasi

    print("\n[✔] SUCCESS: Quorum Reached. Quantum State Collapsed to VALID.")
    print("[✔] Block recorded in Genesis Ledger.")

if __name__ == "__main__":
    run_simulation()
