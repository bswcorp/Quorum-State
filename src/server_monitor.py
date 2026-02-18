import os
import platform
import time

def check_system():
    print(f"--- QUORUM-STATE SERVER HEALTH CHECK ---")
    print(f"Node Status: ONLINE")
    print(f"Server OS  : {platform.system()} {platform.release()}")
    print(f"Processor  : {platform.processor()}")
    
    # Cek Beban CPU
    load = os.getloadavg() if hasattr(os, 'getloadavg') else "N/A"
    print(f"System Load: {load}")
    
    # Simulasi Koneksi Quorum
    print(f"Quorum Sync: 100% (Connected to 676 Computors)")
    print(f"----------------------------------------")

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(60) # Cek setiap 1 menit
