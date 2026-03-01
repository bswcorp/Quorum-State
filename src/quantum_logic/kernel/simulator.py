
from src.quantum_logic.kernel.h2k_bridge import H2KBridge
from src.quantum_logic.kernel.kernel_sync import KernelSync

def run_v3_simulation():
    print("--- [QUORUM-STATE v3.0.0] SIMULATOR START ---")
    
    # 1. Inisialisasi Jaringan h2k
    bridge = H2KBridge()
    sync = KernelSync()
    
    # 2. Simulasi Transmisi Data
    data = "Quantum_Payload_Alpha_001"
    connection = bridge.connect_to_kernel(data)
    
    if connection['status'] == "H2K_STABLE":
        print(f"[OK] h2k Connection Established. Checksum: {connection['checksum']}")
        
        # 3. Sinkronisasi ke 676 Node
        sync_result = sync.broadcast_to_nodes(connection['checksum'])
        print(f"[OK] {sync_result['nodes_reached']} Nodes Synchronized. Status: {sync_result['status']}")
    
    print("--- [SIMULATION SUCCESSFUL] PERFECT H2K ---")

if __name__ == "__main__":
    run_v3_simulation()
