import requests
import os
import platform
from datetime import datetime

# KONFIGURASI TELEGRAM (MASUKKAN TOKEN & ID ANDA)
TOKEN = "GANTI_DENGAN_TOKEN_BOTFATHER"
CHAT_ID = "GANTI_DENGAN_ID_USERINFOBOT"

def send_welcome_message():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_info = f"Model: {platform.node()}\nKernel: {platform.release()}"
    
    message = (
        "🚀 *SYSTEM ONLINE: QUORUM-STATE GENESIS*\n\n"
        f"Selamat Datang, *Capo*! 🍻\n"
        "Server **IBM System x3250 M2** telah berhasil melakukan 'First Boot' di Bintaro.\n\n"
        f"📅 *Waktu:* {timestamp}\n"
        f"🖥️ *Info:* {server_info}\n"
        "🛡️ *Status:* Quantum-Shield Active\n\n"
        "--- *The Last Safe Haven Before Q-Day* ---"
    )
    
    url = f"https://api.telegram.org{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        requests.post(url, data=payload)
        print("[🚀] Pesan selamat datang berhasil dikirim ke Telegram!")
    except Exception as e:
        print(f"[✘] Gagal kirim pesan: {e}")

if __name__ == "__main__":
    send_welcome_message()
