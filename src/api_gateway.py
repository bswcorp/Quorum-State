from flask import Flask, render_template_string
import json

app = Flask(__name__)

# DATA STRATEGI GODFATHER: 10% dipecah ke 10 Tahap (1% per tahap)
# Harga naik Rp100 setiap tahapnya
price_stages = [
    {"tahap": 1, "harga": 100, "volume": "10M"},
    {"tahap": 2, "harga": 200, "volume": "10M"},
    {"tahap": 3, "harga": 300, "volume": "10M"},
    {"tahap": 4, "harga": 400, "volume": "10M"},
    {"tahap": 5, "harga": 500, "volume": "10M"},
    {"tahap": 6, "harga": 600, "volume": "10M"},
    {"tahap": 7, "harga": 700, "volume": "10M"},
    {"tahap": 8, "harga": 800, "volume": "10M"},
    {"tahap": 9, "harga": 900, "volume": "10M"},
    {"tahap": 10, "harga": 1000, "volume": "10M"}
]

labels = [d['tahap'] for d in price_stages]
prices = [d['harga'] for d in price_stages]

DASHBOARD_CHART = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QSTATE | Price Discovery</title>
    <script src="https://cdn.jsdelivr.net"></script>
    <style>
        body { background: #000b14; color: #00e5ff; font-family: sans-serif; padding: 20px; text-align: center; }
        .chart-container { background: #001a2e; padding: 15px; border-radius: 15px; border: 1px solid #004466; margin-top: 20px; }
        h1 { font-size: 20px; text-shadow: 0 0 10px #00e5ff; }
        .info { font-size: 12px; margin-top: 20px; color: #7FDBFF; }
    </style>
</head>
<body>
    <h1>📈 GRAFIK DISTRIBUSI 10% ($QSTATE)</h1>
    <p style="font-size: 10px;">Strategi Harga Bertahap (Anti-Dumping)</p>

    <div class="chart-container">
        <canvas id="priceChart"></canvas>
    </div>

    <div class="info">
        <p>Status: <b>TAHAP 1 AKTIF (Rp. 100)</b></p>
        <p>Volume per Tahap: 10.000.000 $QSTATE (1%)</p>
    </div>

    <script>
        const ctx = document.getElementById('priceChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: {{ labels | safe }},
                datasets: [{
                    label: 'Harga (IDR)',
                    data: {{ prices | safe }},
                    borderColor: '#00e5ff',
                    backgroundColor: 'rgba(0, 229, 255, 0.1)',
                    borderWidth: 3,
                    stepped: true, // INI KUNCINYA: Membuat grafik berbentuk tangga
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { grid: { color: '#004466' }, ticks: { color: '#fff' } },
                    x: { grid: { display: false }, ticks: { color: '#fff' } }
                },
                plugins: { legend: { display: false } }
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def chart_page():
    return render_template_string(DASHBOARD_CHART, labels=json.dumps(labels), prices=json.dumps(prices))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
