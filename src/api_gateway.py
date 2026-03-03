from flask import Flask, render_template_string
import sys
import os

# Hubungkan ke Core Mesin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from qstate_core import QuorumStateCore

app = Flask(__name__)
node = QuorumStateCore()

# Simulasi Operasi Packman (Langsung Mengisi Bunker)
node.activate_packman(10000000) # Hisap 10jt, Muntahkan 2jt ke Rakyat

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QSTATE | Monitor Keadilan</title>
    <style>
        body { background: #00050a; color: #00e5ff; font-family: sans-serif; padding: 20px; text-align: center; }
        .bunker-tank { 
            width: 150px; height: 250px; border: 4px solid #00e5ff; 
            margin: 30px auto; position: relative; border-radius: 0 0 15px 15px;
            background: rgba(0,229,255,0.05); overflow: hidden; box-shadow: 0 0 30px rgba(0,229,255,0.2);
        }
        .liquid { 
            position: absolute; bottom: 0; width: 100%; 
            background: linear-gradient(to top, #0074D9, #7FDBFF);
            height: 65%; transition: height 2s ease-in-out;
        }
        .stats { background: #001a2e; padding: 20px; border-radius: 15px; border: 1px solid #004466; margin-top: 20px; }
        .btn-muntah { background: #ff0055; color: white; border: none; padding: 15px; border-radius: 10px; width: 100%; font-weight: bold; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>🏦 BUNKER RAKYAT MONITOR</h1>
    <p>Visualisasi Distribusi Bab 15</p>

    <div class="bunker-tank">
        <div class="liquid"></div>
    </div>

    <div class="stats">
        <div style="font-size: 11px; color: #7FDBFF;">SALDO TERKUNCI UNTUK RAKYAT</div>
        <div style="font-size: 24px; font-weight: bold; margin: 10px 0;">{{ bunker_bal }} $QSTATE</div>
        <div style="color: #2ECC40; font-size: 12px; font-weight: bold;">● PACKMAN FEEDING ACTIVE</div>
    </div>

    <button class="btn-muntah" onclick="alert('Bansos Berhasil Dimuntahkan ke Rakyat via Eye-ID!')">MUNTAHKAN BANSOS (EYE-ID)</button>

    <div style="margin-top: 40px; font-size: 10px; color: #004466;">
        DASHBOARD KEADILAN | VISI: ANDI MUHAMMAD HARPIANTO
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    bal = "{:,}".format(node.get_balance("BUNKER-RAKYAT-MISKIN"))
    return render_template_string(DASHBOARD_HTML, bunker_bal=bal)

if __name__ == '__main__':
    # NYC Port 8000 untuk Mobile Access
    app.run(host='0.0.0.0', port=8000, debug=True)
