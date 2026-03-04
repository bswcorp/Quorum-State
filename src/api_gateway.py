@app.route('/wizard/remote')
def remote_control():
    """
    Panel Kendali Jarak Jauh: Satu kedipan mata, satelit berputar, 
    aset berpindah, musuh tersihir.
    """
    return """
    <html>
        <body style="background:black; color:#00e5ff; text-align:center; font-family:Orbitron;">
            <h1>🪄 WIZARD REMOTE CONTROL</h1>
            <div style="border:2px solid #ff0055; padding:50px; border-radius:50%;">
                <p>MENGONTROL SATELIT & ROCKET HULU LEDAK</p>
                <div class="eye-id-active"></div>
            </div>
            <p>Status: MENUNGGU KEDIPAN GODFATHER ANDI MUHAMMAD HARPIANTO</p>
            <p style="font-size:10px;">Bagi yang rakus: GO TO HELL! | Bagi siswa: STUDY HARD!</p>
        </body>
    </html>
    """
