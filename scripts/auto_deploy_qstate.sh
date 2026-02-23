#!/bin/bash
# AUTO-DEPLOYMENT $QSTATE QUANTUM PAC-MAN
# Lokasi: Command Center Ubuntu Lenovo

echo "🚀 [INIT] Membangun Benteng $QSTATE..."
sleep 2

# Cek Integritas NIST Script
if [ -f "scripts/quantum_pacman_core.py" ]; then
    echo "✅ [VALID] NIST Core Terdeteksi."
else
    echo "❌ [ERROR] Core Hilang! Jalankan Recovery GitHub..."
    exit 1
fi

# Jalankan Mesin Kanibal dalam Mode Background
nohup python3 scripts/quantum_pacman_core.py > logs/pacman_live.log 2>&1 &
echo "🔥 [ACTIVE] Quantum Pac-Man sedang 'Memangsa' Keraguan Dunia di Background."
