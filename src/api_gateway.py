from flask import Flask, render_template_string, jsonify
import sys
import os

# Menghubungkan ke Mesin Inti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from qstate_core import QuorumStateCore

app = Flask(__name__)
central_bank = QuorumStateCore()
central_bank.mint("TREASURY-RESERVE", 1000000000000)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>QSTATE | Quantum Central Bank</title>
    <style>
        body { font-family: 'Orbitron', sans-serif; background: #00050a; color: #00e5ff; padding: 20px; text-align: center; }
        .main-frame { border: 2px solid #00e5ff; border-radius: 30px; padding: 40px; background: rgba(0,20,40,0.9); box-shadow: 0 0 100px #003344; max-width: 900px; margin: auto; }
        .stat-box { display: flex; justify-content: space-around; margin-bottom: 40px; border-bottom: 1px solid #004466; padding-bottom: 20px; }
        .feature-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
        .feature-card { border: 1px solid #00e5ff; padding: 20px; border-radius: 20px; background: #001a2e; }
        .qris-box { background: white; padding: 10px; display: inline-block; border-radius: 10px; margin-top: 10px; }
        .eye-scanner { border: 2px solid #ff0055; height: 100px; border-radius: 50% 50% 0 0; position: relative; overflow: hidden; background: #1a0008; }
        .scanner-line { width: 100%; height: 2px; background: #ff0055; position: absolute; animation: scan 2s infinite; }
        @keyframes scan { from { top: 0; } to { top: 100%; } }
        h1 { font-size: 28px; text-transform: uppercase; letter-spacing: 5px; color: white; }
    </style>
</head>
<body>
    <div class="main-frame">
        <h1>🏦 QSTATE CENTRAL BANK v.2026</h1>
        
        <div class="stat-box">
            <div><small>TREASURY RESERVE</small><br><b>{{ treasury_balance }} $QSTATE</b></div>
            <div><small>SECURITY</small><br><b style="color:#00ff88;">QUANTUM-ACTIVE</b></div>
        </div>

        <div class="feature-grid">
            <!-- FITUR QRIS & BARCODE -->
            <div class="feature-card">
                <h3>📲 QRIS & BARCODE PAY</h3>
                <div class="qris-box">
                    <img src="https://api.qrserver.com" alt="QRIS QSTATE">
                </div>
                <p><small>Scan untuk Transaksi Kuantum Instan</small></p>
            </div>

            <!-- FITUR DETEKSI MATA (BIOMETRIC) -->
            <div class="feature-card">
                <h3>👁️ EYE IDENTITY SCAN</h3>
                <div class="eye-scanner">
                    <div class="scanner-line"></div>
                </div>
                <p><small style="color:#ff0055;">Menunggu Pemindaian Biometrik Mata...</small></p>
                <button style="background:#ff0055; border:none; color:white; padding:5px 15px; border-radius:5px; cursor:pointer;">START SCAN</button>
            </div>
        </div>

        <div style="margin-top:40px;">
            <h3>📊 NYC MARKET INDEX: <span style="color:white;">35,420.12 ({{ change }})</span></h3>
        </div>

        <p style="margin-top:50px; font-size:10px;">OPERATIONAL TERMINAL | VISI ANDI MUHAMMAD HARPIANTO</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    balance = "{:,}".format(central_bank.get_balance("TREASURY-RESERVE"))
    return render_template_string(HTML_TEMPLATE, treasury_balance=balance, change="+0.45%")

if __name__ == '__main__':
    # Jika port 5000 bermasalah, ganti ke 8080
    app.run(host='0.0.0.0', port=5000, debug=True)
