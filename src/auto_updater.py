import os
import subprocess
import time

def sync_with_github():
    print(f"--- QUORUM-STATE AUTO-SYNC SYSTEM ---")
    try:
        # Menarik perubahan terbaru dari cabang main di GitHub
        print("[*] Mengecek pembaruan di GitHub...")
        result = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True, text=True)
        
        if "Already up to date" in result.stdout:
            print("[✔] Kode sudah versi terbaru.")
        else:
            print("[🚀] Pembaruan terdeteksi dan berhasil diunduh!")
            # Di sini Anda bisa menambahkan perintah restart service jika diperlukan
            
    except Exception as e:
        print(f"[✘] Gagal sinkronisasi: {e}")

if __name__ == "__main__":
    while True:
        sync_with_github()
        # Melakukan pengecekan setiap 1 jam (3600 detik)
        time.sleep(3600)
