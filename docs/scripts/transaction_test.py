import time
import hashlib

def simulate_qstate_transaction(sender, receiver, amount):
    print(f"🚀 Memulai Transaksi: {amount} $QSTATE dari {sender} ke {receiver}")
    start_time = time.time()
    
    # Simulasi Enkripsi NIST-compliant (Lattice-based Hashing)
    tx_data = f"{sender}{receiver}{amount}{start_time}"
    tx_hash = hashlib.sha3_256(tx_data.encode()).hexdigest()
    
    print(f"🔐 Enkripsi NIST Validated: {tx_hash[:16]}...")
    
    # Simulasi Validasi Node Quorum (M2 & M3 Power)
    time.sleep(0.5) # Simulasi latensi jaringan minimal
    
    end_time = time.time()
    duration = end_time - start_time
    
    if duration < 3:
        print(f"✅ TRANSAKSI BERHASIL! Durasi: {duration:.2f} detik.")
        print("💡 Status: INSTANT CONFIRMATION (No Pending)")
    else:
        print(f"⚠️ Warning: Transaksi melambat ({duration:.2f}s). Cek Load Node!")

# Test Run
simulate_qstate_transaction("Admin_Bintaro", "User_Global", 1000)
