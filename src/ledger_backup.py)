import shutil
import os
import time
from datetime import datetime

# Path sumber ledger dan tujuan backup
LEDGER_PATH = "/home/capo/Quorum-State/src/quantum_logic/ledger_data.json"
BACKUP_DIR = "/home/capo/Quorum-State/backups/"

def perform_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"[*] Membuat direktori backup: {BACKUP_DIR}")

    if os.path.exists(LEDGER_PATH):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{BACKUP_DIR}ledger_backup_{timestamp}.json"
        
        try:
            shutil.copy2(LEDGER_PATH, backup_file)
            print(f"[✔] Backup Berhasil: {backup_file}")
            
            # Hapus backup lama (sisakan 10 file terakhir)
            backups = sorted([f for f in os.listdir(BACKUP_DIR) if f.startswith("ledger_backup_")])
            if len(backups) > 10:
                for old_backup in backups[:-10]:
                    os.remove(os.path.join(BACKUP_DIR, old_backup))
                    print(f"[-] Menghapus backup lama: {old_backup}")
        except Exception as e:
            print(f"[✘] Gagal melakukan backup: {e}")
    else:
        print("[!] File Ledger tidak ditemukan. Pastikan transaksi sudah berjalan.")

if __name__ == "__main__":
    print(f"--- QUORUM-STATE AUTOMATIC BACKUP SYSTEM ---")
    while True:
        perform_backup()
        # Backup setiap 6 jam
        time.sleep(21600) 
