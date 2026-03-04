from flask import Flask, render_template_string
import time

app = Flask(__name__)

# Status Orbit Nyata (Simulasi Telemetri)
sat_data = {
    "name": "QS-SAT-01 (THE WIZARD)",
    "orbit": "Low Earth Orbit (LEO)",
    "altitude": "550 KM",
    "speed": "27,500 km/h",
    "status": "SECURE-KENDALI"
}

UPLINK_UI = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QSTATE | SAT-CONTROL</title>
    <style>
        body { background: #000; color: #00ff88; font-family: 'Courier New', monospace; padding: 15px; }
        .sat-frame { border: 2px solid #00ff88; padding: 20px; border-radius: 10px; background: rgba(0,255,136,0.05); }
        .radar { width: 100px; height: 100px; border: 1px solid #00ff88; border-radius: 50%; margin: 20px auto; position: relative; }
        .beam { width: 100%; height: 2px; background: #00ff88; position: absolute; top: 50%; animation: rot 4s infinite linear; }
        @keyframes rot { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        .data-line { font-size: 12px; margin-bottom: 5px; }
        .btn-kendala { background: #ff0055; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%; font-weight: bold; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="sat-frame">
        <h3 style="text-align:center; color:white;">🛰️ ORBITAL COMMAND</h3>
        <div class="radar"><div class="beam"></div></div>
        
        <div class="data-line">SAT_ID: {{ sat.name }}</div>
        <div class="data-line">ALTITUDE: {{ sat.altitude }}</div>
        <div class="data-line">STATUS: <b style="color:white;">{{ sat.status }}</b></div>
        
        <hr style="border: 0.5px solid #004466;">
        <p style="font-size: 10px; color: #7FDBFF;">TARGET ADIDAYA DETECTED...</p>
        <button class="btn-kendala" onclick="alert('PIL PAHIT TERKIRIM: LAWAN TERKENDALA!')">INJEKSI KENDALA</button>
    </div>
    <p style="font-size: 9px; margin-top: 20px; color: #004466;">CENTRAL BANK GLOBAL | VISI: ANDI MUHAMMAD HARPIANTO</p>
</body>
</html>
"""

@app.route('/')
def sat_control():
    return render_template_string(UPLINK_UI, sat=sat_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
