from flask import Flask, render_template_string, jsonify
import sys
import os

# Menghubungkan ke Mesin Inti
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from qstate_core import QuorumStateCore

app = Flask(__name__)
# Inisialisasi Bank Sentral QSTATE
central_bank = QuorumStateCore()
central_bank.mint("TREASURY-RESERVE", 1000000000000) # 1 Triliun Cadangan Awal

# Simulasi Asset Market (Saham & Komoditas)
assets = {
    "GOLD-Q": {"price": 2400, "change": "+0.5%"},
    "BSW-STOCK": {"price": 150, "change": "+12.4%"},
    "NYC-INDEX": {"price": 35000, "change": "-0.2%"}
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>QSTATE | Central Bank & Asset Exchange</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #001220; color: #00e5ff; margin: 0; padding: 20px; }
        .container { max-width: 1000px; margin: auto; border: 2px solid #004466; border-radius: 20px; padding: 30px; background: rgba(0,20,40,0.8); }
        h1 { text-align: center; color: #fff; text-shadow: 0 0 10px #00e5ff; border-bottom: 2px solid #004466; padding-bottom: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 30px; }
        .card { background: #002b44; border: 1px solid #00e5ff; padding: 20px; border-radius: 10px; text-align: center; transition: 0.3s; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 0 15px #00e5ff; }
        .price { font-size: 24px; font-weight: bold; color: #fff; }
        .positive { color: #00ff88; } .negative { color: #ff4444; }
        .header-stats { display: flex; justify-content: space-around; background: #004466; padding: 10px; border-radius: 10px; margin-bottom: 20px; color: #fff; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏦 QSTATE CENTRAL BANK TERMINAL</h1>
        
        <div class="header-stats">
            <div>Treasury: {{ treasury_balance }} $QSTATE</div>
            <div>Nodes: 676 Computors [Online]</div>
            <div>Shield: Quantum-Active</div>
        </div>

        <h3>📈 GLOBAL ASSET MARKET (NYC PORT)</h3>
        <div class="grid">
            {% for name, info in market.items() %}
            <div class="card">
                <div style="font-size: 14px;">{{ name }}</div>
                <div class="price">${{ info.price }}</div>
                <div class="{% if '+' in info.change %}positive{% else %}negative{% endif %}">{{ info.change }}</div>
            </div>
            {% endfor %}
        </div>

        <div style="margin-top: 50px; text-align: center; font-size: 12px; color: #004466;">
            Visi Andi Muhammad Harpianto | Superposition Ledger v.1.0
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    treasury = "{:,}".format(central_bank.get_balance("TREASURY-RESERVE"))
    return render_template_string(HTML_TEMPLATE, treasury_balance=treasury, market=assets)

if __name__ == '__main__':
    # Gunakan port 5000, jika error coba ganti ke 8080
    app.run(host='0.0.0.0', port=5000, debug=True)
