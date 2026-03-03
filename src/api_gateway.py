from flask import Flask, render_template_string, request, jsonify
import sys
import os

# Hubungkan ke Core Mesin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from qstate_core import QuorumStateCore

app = Flask(__name__)
node = QuorumStateCore()
node.mint("BSW-RESERVE-ANDI", 75000000)

# Data Wahana Voting (Proposal Aktif)
governance = {
    "proposal_id": "QS-PROP-001",
    "title": "Upgrade Keamanan Quantum Shield v.2",
    "yes_votes": 450,
    "no_votes": 20,
    "status": "VOTING_PERIOD"
}

MOBILE_VOTING_UI = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QSTATE Governance</title>
    <style>
        body { background: #00050a; color: #00e5ff; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 15px; }
        .app-bar { text-align: center; border-bottom: 2px solid #004466; padding: 15px; font-weight: bold; }
        .prop-card { background: #001a2e; border: 1px solid #00e5ff; border-radius: 15px; padding: 20px; margin-top: 20px; }
        .voting-bar { height: 10px; background: #004466; border-radius: 5px; margin: 15px 0; position: relative; overflow: hidden; }
        .yes-progress { height: 100%; background: #2ECC40; width: 85%; }
        .eye-verify { border: 2px solid #ff0055; width: 60px; height: 60px; border-radius: 50%; margin: 10px auto; position: relative; }
        .scan { width: 100%; height: 2px; background: #ff0055; position: absolute; animation: s 1s infinite; }
        @keyframes s { from { top: 0; } to { top: 100%; } }
        .btn-group { display: flex; gap: 10px; margin-top: 20px; }
        .btn { flex: 1; padding: 15px; border-radius: 10px; border: none; font-weight: bold; color: white; cursor: pointer; }
        .btn-yes { background: #2ECC40; } .btn-no { background: #ff4444; }
    </style>
</head>
<body>
    <div class="app-bar">🗳️ QSTATE GOVERNANCE</div>
    
    <div class="prop-card">
        <div style="font-size: 10px; color: #7FDBFF;">PROPOSAL #{{ prop.proposal_id }}</div>
        <h3 style="margin: 10px 0;">{{ prop.title }}</h3>
        
        <div class="eye-verify"><div class="scan"></div></div>
        <div style="text-align:center; font-size: 10px; color:#ff0055;">VERIFIKASI MATA AKTIF</div>

        <div class="voting-bar"><div class="yes-progress"></div></div>
        <div style="display: flex; justify-content: space-between; font-size: 12px;">
            <span>YEA: {{ prop.yes_votes }}</span>
            <span>NAY: {{ prop.no_votes }}</span>
        </div>

        <div class="btn-group">
            <button class="btn btn-yes" onclick="vote('YEA')">VOTE YES</button>
            <button class="btn btn-no" onclick="vote('NAY')">VOTE NO</button>
        </div>
    </div>

    <div style="margin-top: 30px; text-align: center; font-size: 10px; color: #004466;">
        WAHANA VOTING TERDESENTRALISASI | VISI ANDI MUHAMMAD HARPIANTO
    </div>

    <script>
        function vote(choice) {
            alert("Suara " + choice + " Anda telah dikunci oleh Quorum-State Shield!");
            if(window.navigator.vibrate) window.navigator.vibrate(100);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def governance_page():
    return render_template_string(MOBILE_VOTING_UI, prop=governance)

if __name__ == '__main__':
    # NYC Port 8000 - Standar untuk Mobile Access
    app.run(host='0.0.0.0', port=8000, debug=True)
