from flask import Flask, render_template, jsonify
import sys
import os

# Hubungkan ke Core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
from qstate_core import QuorumStateCore

app = Flask(__name__)
node = QuorumStateCore()

# Data awal untuk Genesis
node.mint("BSW-LABS-GENESIS", 200000000)

@app.route('/')
def dashboard():
    """Tampilan Utama Wallet & Explorer"""
    data = {
        "supply": node.total_supply,
        "max_supply": node.MAX_SUPPLY,
        "nodes": node.consensus.total_computors,
        "shield": "ACTIVE" if node.shield_active else "INACTIVE"
    }
    return f"""
    <html>
        <head><title>Quorum-State Dashboard</title>
        <style>
            body {{ font-family: sans-serif; background: #001f3f; color: white; text-align: center; padding: 50px; }}
            .card {{ background: #0074D9; padding: 20px; border-radius: 15px; display: inline-block; margin: 10px; width: 250px; }}
            h1 {{ color: #7FDBFF; }}
            .status {{ color: #2ECC40; font-weight: bold; }}
        </head>
        <body>
            <h1>$QSTATE EXPLORER & WALLET</h1>
            <div class="card"><h3>Total Supply</h3><p>{data['supply']:,}</p></div>
            <div class="card"><h3>Max Supply</h3><p>200T</p></div>
            <div class="card"><h3>Active Computors</h3><p>{data['nodes']}</p></div>
            <div class="card"><h3>Quantum Shield</h3><p class="status">{data['shield']}</p></div>
            <br><br>
            <p><i>Visi Andi Muhammad Harpianto: "Catch MyCat U CanGet MyCheque"</i></p>
        </body>
    </html>
    """

@app.route('/api/stats')
def get_stats():
    return jsonify({
        "total_supply": node.total_supply,
        "computors": node.consensus.total_computors
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
