import sys
import os

# --- PENYANGGA NAVIGASI (PENTING) ---
# Mengambil path folder 'quantum_logic' agar kernel bisa mengintip ke luar
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Sekarang Anda bisa memanggil modul lain tanpa error
from h2k_bridge import h2k_bridge  # Pastikan nama fungsi di h2k_bridge.py sesuai
from quantum_shield import QuantumShield
from quantum_ledger import QuantumLedger

class QuorumKernel:
    """Inti Operasional Quorum-State"""
    def __init__(self):
        print("[Kernel] Menghidupkan Hyper-to-Kernel Bridge...")
        # Panggil h2k_bridge yang diimpor dari luar
        h2k_bridge("INITIALIZING_KERNEL") 

# ... sisa kode simulator Anda ...
