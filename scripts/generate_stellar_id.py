import hashlib
import time

def create_stellar_id(name, geek_code):
    print(f"🆔 [ID-GEN] Mencetak Kartu untuk: {name}")
    
    # Generate Unique Hash sebagai ID Kepesertaan
    seed = f"{name}{geek_code}{time.time()}"
    stellar_hash = hashlib.sha3_256(seed.encode()).hexdigest()[:12].upper()
    
    print("------------------------------------------")
    print(f"🌟 QUORUM-STATE STELLAR ID 🌟")
    print(f"ID     : QST-{stellar_hash}")
    print(f"NAME   : {name}")
    print(f"GEEK   : {geek_code}")
    print(f"STATUS : ACTIVE - NIST PQC PROTECTED")
    print("------------------------------------------")
    
    return f"QST-{stellar_hash}"

# Contoh Running untuk Siswa Pertama
create_stellar_id("ANDI MUHAMMAD HARPIANTO JR", "GCS d- s: a-- C++ UL++++")
