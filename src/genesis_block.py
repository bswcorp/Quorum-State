import hashlib
import json
import time

def create_genesis_block():
    print(f"--- QUORUM-STATE GENESIS BLOCK GENERATOR ---")
    
    # Data transaksi pertama dalam sejarah $QSTATE
    genesis_data = {
        "index": 1,
        "timestamp": time.ctime(),
        "message": "The Last Safe Haven Before Q-Day",
        "founder": "Capo & BreSpeedWorks Labs",
        "infrastructure": "IBM System x3650 M3",
        "network_probe": "RIPE-Atlas Active",
        "previous_hash": "0" * 64
    }
    
    # Menghasilkan Hash suci untuk blok pertama
    block_string = json.dumps(genesis_data, sort_keys=True).encode()
    genesis_hash = hashlib.sha3_256(block_string).hexdigest()
    
    genesis_data["hash"] = genesis_hash
    
    # Simpan sebagai file ledger awal
    with open("src/quantum_logic/ledger_data.json", "w") as f:
        json.dump([genesis_data], f, indent=4)
    
    print(f"[🚀] GENESIS BLOCK CREATED!")
    print(f"Hash: {genesis_hash}")
    print(f"Status: QUANTUM_STABLE")

if __name__ == "__main__":
    create_genesis_block()
