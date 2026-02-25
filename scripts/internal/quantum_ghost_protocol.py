import os
import random

def activate_ghost_protocol():
    print("👻 [GHOST] Mengaktifkan Protokol Siluman...")
    # Logika: Mengacak MAC Address & Mengganti Hostname Server
    new_host = f"QST-NODE-GHOST-{random.randint(100, 999)}"
    os.system(f"sudo hostnamectl set-hostname {new_host}")
    print(f"✅ [STATUS] Server kini tidak terdeteksi. Identitas Baru: {new_host}")

if __name__ == "__main__":
    activate_ghost_protocol()
