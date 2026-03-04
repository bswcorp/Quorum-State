from flask import Flask, render_template_string, jsonify
import sys
import os

# Hubungkan ke Telemetri
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from satellite_telemetry import SatelliteTelemetry

app = Flask(__name__)
sat_engine = SatelliteTelemetry()

TELEMETRY_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QSTATE | SATELLITE RADAR</title>
    <style>
        body { background: #000b14; color: #00e5ff; font-family: 'Courier New', monospace; padding: 20px; text-align: center; }
        .radar-box { border: 2px solid #00e5ff; border-radius: 20px; padding: 20px; background: rgba(0,229,255,0.05); box-shadow: 0 0 20px #004466; }
        .glitch { font-size: 1.5em; font-weight: bold; text-transform: uppercase; color: #fff; text-shadow: 2px 2px #ff0055; }
        .telemetry-grid { display: grid; grid-template-columns: 1fr; gap: 10px; margin-top: 20px; text-align: left; font-size: 0.9em; }
        .data-val { color: #00ff88; float: right; }
        .blink { animation: blinker 1s linear infinite; color: #ff0055; }
        @keyframes blinker { 50% { opacity: 0; } }
    </style>
</head>
<body>
    <div class="radar-box">
        <div class="glitch">QS-SAT-01 UPLINK</div>
        <p class="blink">● TRANSMISSION ENCRYPTED</p>
        <hr style="border: 0.5px solid #004466;">
        
        <div id="data-display" class="telemetry-grid">
            <!-- Data akan diisi via AJAX agar Real-time -->
            <div>Memuat Koordinat Langit...</div>
        </div>
        
        <button onclick="location.reload()" style="margin-top:20px; background:#004466; color:white; border:none; padding:10px; border-radius:5px;">RE-SCAN ORBIT</button>
    </div>
    <p style="font-size: 0.7em; margin-top: 30px; color: #004466;">KEDAULATAN ORBITAL | VISI ANDI MUHAMMAD HARPIANTO</p>

    <script>
        function updateData() {
            fetch('/api/telemetry')
                .then(response => response.json())
                .then(data => {
                    let html = `
                        <div>SATID: <span class="data-val">${data.sat_id}</span></div>
                        <div>COORD: <span class="data-val">${data.coords}</span></div>
                        <div>ALTIT: <span class="data-val">${data.altitude}</span></div>
                        <div>TIME : <span class="data-val">${data.timestamp}</span></div>
                        <div>SIG  : <span class="data-val">${data.signal}</span></div>
                        <div>STAT : <span class="data-val" style="color:#fff;">${data.status}</span></div>
                    `;
                    document.getElementById('data-display').innerHTML = html;
                });
        }
        setInterval(updateData, 3000); // Update setiap 3 detik
        updateData();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TELEMETRY_HTML)

@app.route('/api/telemetry')
def api_telemetry():
    return jsonify(sat_engine.get_live_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
