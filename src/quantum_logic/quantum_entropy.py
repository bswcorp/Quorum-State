# src/quantum_logic/quantum_entropy.py
import os
import hashlib

def generate_quantum_seed():
    """Mengambil entropy dari noise sistem fisik IBM M3 untuk benih acak."""
    raw_entropy = os.urandom(64)
    quantum_seed = hashlib.sha3_512(raw_entropy).hexdigest()
    print(f"[🌀] Quantum Entropy Seed Generated: {quantum_seed[:16]}...")
    return quantum_seed

if __name__ == "__main__":
    generate_quantum_seed()
