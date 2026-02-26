import hashlib
import time

def generate_bio_key(heart_rate_bpm, oxygen_level):
    """
    Simulasi konversi frekuensi jantung (IoB) menjadi Private Key NIST.
    """
    print(f"💓 [IoB] Mensinkronisasi Detak Jantung: {heart_rate_bpm} BPM")
    
    # Menyatukan data biologis menjadi seed (benih) kriptografi
    bio_data = f"HEART:{heart_rate_bpm}-O2:{oxygen_level}-{time.strftime('%Y%m%d')}"
    
    # NIST SHA-3 512 untuk Keamanan Maksimal
    private_key = hashlib.sha3_512(bio_data.encode()).hexdigest()
    
    print("✅ [SUCCESS] Biological Private Key Terbentuk!")
    print(f"🗝️ Key: {private_key[:32]}...[LOCKED BY NIST]")
    return private_key

# Contoh: User dengan detak jantung 72 BPM dan Oksigen 98%
my_bio_key = generate_bio_key(72, 98)
