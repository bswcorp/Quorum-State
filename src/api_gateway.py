from flask import Flask, render_template_string
import sys
import os

# Menghubungkan ke Mesin Inti di src/core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from qstate_core import QuorumStateCore

app = Flask(__name__)
node = QuorumStateCore()
# Saldo Awal untuk Reserve Mobile Andi Muhammad Harpianto
node.mint("BSW-RESERVE-ANDI", 75000000)

MOBILE_UI = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>QSTATE Mobile Central Bank</title>
    <style>
        body { background: #000b14; color: #00e5ff; font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }
        .app-bar { background: #001a2e; padding: 15px; text-align: center; border-bottom: 2px solid #004466; font-weight: bold; letter-spacing: 2px; }
        .balance-card { background: linear-gradient(135deg, #004466 0%, #001a2e 100%); margin: 20px; padding: 25px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.5); border: 1px solid #00e5ff; }
        .eye-auth { width: 140px; height: 140px; border: 3px solid #ff0055; border-radius: 50%; margin: 30px auto; position: relative; box-shadow: 0 0 30px #ff0055; background: radial-gradient(circle, #2a000a 0%, #000 70%); }
        .scan-line { width: 100%; height: 4px; background: #ff0055; position: absolute; animation: scan 2s infinite ease-in-out; box-shadow: 0 0 15px #ff0055; }
        @keyframes scan { 0% { top: 0; } 50% { top: 100%; } 100% { top: 0; } }
        .action-btns { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; padding: 20px; }
        .btn { background: #0074D9; color: white; border: none; padding: 18px; border-radius: 15px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 10px rgba(0,116,217,0.3); }
        .footer { margin-top: auto; padding: 20px; text-align: center; font-size: 11px; color: #004466; letter-spacing: 1px; }
        .qris-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: black; display: none; flex-direction: column; align-items: center; justify-content: center; z-index: 100; }
    </style>
</head>
<body>
    <div class="app-bar">🏛️ QSTATE CENTRAL MOBILE</div>
    
    <div class="balance-card">
        <div style="font-size: 12px; color: #7FDBFF; text-transform: uppercase;">Total Aset Kuantum</div>
        <div style="font-size: 34px; font-weight: bold; margin-top: 10px;">{{ balance }} <span style="font-size: 16px;">$QSTATE</span></div>
        <div style="font-size: 11px; margin-top: 10px; color: #2ECC40;">● Quantum Shield Active</div>
    </div>

    <div class="eye-auth" onclick="startScan()">
        <div class="scan-line"></div>
        <div style="position:absolute; top:45%; width:100%; text-align:center; font-size:11px; color:white; font-weight:bold;">EYE-ID SCAN</div>
    </div>
    <div id="status" style="text-align:center; font-size: 12px; color:#ff0055; font-weight:bold;">SENTUH UNTUK OTENTIKASI MATA</div>

    <div class="action-btns">
        <button class="btn" onclick="openQRIS()">SCAN QRIS</button>
        <button class="btn" style="background:#004466;" onclick="location.reload()">REFRESH</button>
    </div>

    <div class="footer">
        DASHBOARD OPERASIONAL MOBILE v1.0<br>
        VISI ANDI MUHAMMAD HARPIANTO | BSW CORP
    </div>

    <div id="qris" class="qris-overlay" onclick="this.style.display='none'">
        <h2 style="color:white;">MENUNGGU KAMERA...</h2>
        <div style="background:white; padding:20px; border-radius:15px;">
            <img src="https://api.qrserver.com:{{ balance }}" alt="QRIS">
        </div>
        <p style="color:white; margin-top:20px;">Ketuk untuk Kembali</p>
    </div>

    <script>
        function startScan() {
            document.getElementById('status').innerText = "MENYINGKRONKAN STATUS KUANTUM...";
            document.getElementById('status').style.color = "#00e5ff";
            if(window.navigator.vibrate) window.navigator.vibrate([100, 50, 100]);
            setTimeout(() => {
                document.getElementById('status').innerText = "IDENTITAS TERVERIFIKASI ✓";
                document.getElementById('status').style.color = "#2ECC40";
            }, 3000);
        }
        function openQRIS() {
            document.getElementById('qris').style.display = 'flex';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def mobile_home():
    bal = "{:,}".format(node.get_balance("BSW-RESERVE-ANDI"))
    return render_template_string(MOBILE_UI, balance=bal)

if __name__ == '__main__':
    # NYC Port Standard Port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
