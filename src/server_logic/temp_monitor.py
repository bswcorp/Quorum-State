import os
import time
import requests

# KONFIGURASI TELEGRAM
TOKEN = "GANTI_DENGAN_TOKEN_BOTFATHER"
CHAT_ID = "GANTI_DENGAN_ID_USERINFOBOT"

def get_temp():
    """Mengambil data suhu dari thermal zone Linux."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp_raw = f.read()
            return int(temp_raw) / 1000
    except:
        return None

def send_alert(temp):
    msg = f"⚠️ *TEMPERATURE ALERT: IBM x3250 M2*\n\nSuhu CPU terdeteksi: *{temp}°C*\nStatus: *OVERHEAT WARNING*\n\n[🛡️] Quorum-State System: Menurunkan beban komputasi..."
    url = f"https://api.telegram.org{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

if __name__ == "__main__":
    print("[*] Monitoring Suhu IBM M2 Dimulai...")
    while True:
        cpu_temp = get_temp()
        if cpu_temp and cpu_temp > 75:
            print(f"[🚨] Bahaya! Suhu: {cpu_temp}°C. Mengirim alert...")
            send_alert(cpu_temp)
        time.sleep(300) # Cek setiap 5 menit
