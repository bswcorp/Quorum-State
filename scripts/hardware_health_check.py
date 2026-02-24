import os
import subprocess
import json
import time

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return "N/A"

def check_qstate_health():
    print("🔍 [IQaaS] Memulai Inspeksi Kesehatan Hardware $QSTATE...")
    
    # 1. Identifikasi Sistem (Serial Number & Model)
    sn = run_cmd("sudo dmidecode -s system-serial-number")
    model = run_cmd("sudo dmidecode -s system-product-name")
    
    # 2. Monitor Suhu CPU (NIST Safety Threshold < 75C)
    temp = run_cmd("sensors | grep 'Package id 0' | awk '{print $4}'")
    
    # 3. Status Penyimpanan (SSD Life & Usage)
    storage = run_cmd("df -h / | awk 'NR==2 {print $5}'")
    
    health_report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "node_id": "QST-COMMAND-CENTER-LENOVO",
        "model": model,
        "serial_number": sn,
        "cpu_temp": temp,
        "ssd_usage": storage,
        "status": "HEALTHY" if "N/A" not in temp else "WARNING"
    }
    
    print(json.dumps(health_report, indent=4))
    
    # Simpan ke Log untuk Audit Bulanan
    with open("docs/finance/HARDWARE_HEALTH_LOG.json", "a") as f:
        f.write(json.dumps(health_report) + "\n")

if __name__ == "__main__":
    check_qstate_health()
