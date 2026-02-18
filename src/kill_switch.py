import os
import subprocess
import time

# Path untuk file pemicu (Trigger)
KILL_FILE = "/home/capo/Quorum-State/ABORT_MISSION"

def monitor_kill_switch():
    print(f"--- QUORUM-STATE SECURITY MONITOR ---")
    print(f"[*] Menunggu status keamanan...")
    
    while True:
        if os.path.exists(KILL_FILE):
            print(f"[🚨] EMERGENCY KILL-SWITCH AKTIF!")
            print(f"[!] Menghentikan semua layanan Quorum-State...")
            
            # Perintah untuk mematikan service systemd kita
            subprocess.run(['sudo', 'systemctl', 'stop', 'quorum-state.service'])
            subprocess.run(['sudo', 'systemctl', 'stop', 'quorum-backup.service'])
            
            # Menghapus file pemicu setelah dieksekusi
            os.remove(KILL_FILE)
            print(f"[✔] Jaringan Berhasil Dinonaktifkan. Node Aman.")
            break
        
        time.sleep(5) # Cek setiap 5 detik

if __name__ == "__main__":
    monitor_kill_switch()
