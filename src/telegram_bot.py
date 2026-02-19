import requests
import json
import time

class QStateTelegramBot:
    """
    Bot Notifikasi Otomatis Quorum-State.
    Mengirim laporan transaksi langsung ke HP Xiaomi Capo.
    """
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org{self.token}/sendMessage"

    def send_notification(self, message):
        """Mengirim pesan teks ke Telegram."""
        payload = {
            "chat_id": self.chat_id,
            "text": f"🛡️ [QUORUM-STATE SYSTEM REPORT]\n\n{message}\n\nStatus: QUANTUM_STABLE",
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(self.api_url, data=payload)
            return response.json()
        except Exception as e:
            print(f"[✘] Gagal kirim Telegram: {e}")
            return None

if __name__ == "__main__":
    # GANTI DENGAN TOKEN DARI @BotFather DAN CHAT_ID ANDA
    TOKEN = "YOUR_BOT_TOKEN_HERE"
    CHAT_ID = "YOUR_CHAT_ID_HERE"
    
    bot = QStateTelegramBot(TOKEN, CHAT_ID)
    
    # Simulasi Laporan dari IBM x3250 M2
    log_msg = "*TRANSAKSI MASUK*\n💰 Amount: 50,000 $QSTATE\n👤 From: QRIS_GATEWAY\n✅ Status: SUCCESS"
    print("[*] Mencoba mengirim notifikasi ke HP Capo...")
    bot.send_notification(log_msg)
