@echo off
title QUORUM-STATE STARTUP SYSTEM
echo [*] Memulai Infrastruktur Quorum-State...

:: Menjalankan Telegram Welcome Bot
start python src/quantum_logic/welcome_bot.py

:: Menjalankan Monitor Suhu
start python src/server_logic/temp_monitor.py

:: Menjalankan API Bridge
start python src/quantum_logic/api_bridge.py

echo [✔] Semua Sistem Berjalan di Background.
pause
