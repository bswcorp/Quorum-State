import random

def check_quorum(total_nodes=676):
    print(f"📡 [QUORUM] Menghubungi {total_nodes} Computors...")
    
    # Simulasi Suara Node (True = Setuju, False = Tolak/Mati)
    votes = [random.choice([True, True, True, False]) for _ in range(total_nodes)]
    agreed = votes.count(True)
    
    threshold = int(total_nodes * 0.67) # Standar 67%
    
    print(f"🗳️  Hasil Voting: {agreed} Setuju | Threshold: {threshold}")
    
    if agreed >= threshold:
        print("✅ [SUCCESS] Konsensus Tercapai. Transaksi Berdaulat!")
        return True
    else:
        print("❌ [FAILED] Quorum Gagal. Transaksi Ditolak!")
        return False

# Eksekusi Simulasi
check_quorum()
