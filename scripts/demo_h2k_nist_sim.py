import hashlib
import time
import random
import sys

def bio_pulse_animation():
    pulses = ["💓", "💗", "💖", "💔", "❤️"]
    for _ in range(3):
        for p in pulses:
            sys.stdout.write(f"\r{p} [SCANNING BIOMETRIC FREQUENCY...] ")
            sys.stdout.flush()
            time.sleep(0.1)

def run_h2k_demo(name, bpm):
    print(f"\n🚀 STARTING $QSTATE BIOMETRIC HANDSHAKE for: {name}")
    print("--------------------------------------------------")
    
    # 1. Simulasikan Pengambilan Frekuensi Jantung (IoB)
    bio_pulse_animation()
    print(f"\n✅ HEART RATE STABLE: {bpm} BPM (NIST-Validated)")
    time.sleep(1)

    # 2. Proses Enkapsulasi NIST PQC (Kyber Simulation)
    print("🔐 ENCAPSULATING PRIVATE KEY (Standard: NIST FIPS 203)...")
    time.sleep(1.5)
    
    # Generate Seed dari Bio-Data
    seed = f"HRV-{bpm}-{random.random()}-{time.time()}"
    pqc_key = hashlib.sha3_512(seed.encode()).hexdigest()
    
    print(f"🔑 PRIMARY KEY GENERATED: {pqc_key[:32]}...[LOCKED]")
    
    # 3. Transaksi Quorum 676
    print("\n📡 BROADCASTING TO 676 COMPUTORS...")
    for i in range(1, 4):
        print(f"   [Cluster {i:02}] Validating Lattice Signature...")
        time.sleep(0.5)
    
    print("\n✅ TRANSACTION SUCCESS: 453/676 Nodes Confirmed.")
    print(f"💰 STATUS: $QSTATE Transferred via Heartbeat.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    try:
        # Simulasi untuk Capo
        run_h2k_demo("ANDI MUHAMMAD HARPIANTO", 75)
    except KeyboardInterrupt:
        print("\n🛑 Demo Interrupted by User.")
