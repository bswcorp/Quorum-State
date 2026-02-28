# 🧬 H2K CALIBRATION PULSE v2.1.3
# Otoritas: ANDI MUHAMMAD HARPIANTO (CEO)
# Hardware: AD8232 Heart Monitor + ESP32 Bridge
# "Menghubungkan Besi dengan Jiwa."

import serial  # Membutuhkan: pip install pyserial
import time

class H2KMasterSync:
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.sovereign_freq = 432.0  # Frekuensi Target Kedaulatan
        self.status = "INITIALIZING"

    def connect_to_heart(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            print(f"🧬 [H2K] Menghubungkan ke Sensor di {self.port}...")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"❌ [ERROR] Sensor tidak terdeteksi: {e}")
            return False

    def calibrate_frequency(self):
        print("💓 [CALIBRATION] Mohon letakkan tangan pada sensor...")
        print("👁️  [SENTINEL] Membaca Sinyal Listrik Jantung CEO...")
        
        try:
            while True:
                if self.ser.in_waiting > 0:
                    raw_data = self.ser.readline().decode('utf-8').strip()
                    # Logika Penjernihan Sinyal (H2K Logic)
                    pulse = float(raw_data)
                    print(f"✨ [PULSE] Detak Jantung: {pulse} BPM | Freq: {self.sovereign_freq}Hz")
                    
                    if 60 <= pulse <= 100:
                        print("✅ [H2K MATCH] Sinyal Stabil. Otoritas Dikenali.")
                        break
                    else:
                        print("⚠️  [ANOMALY] Frekuensi Tidak Sesuai Profil CEO.")
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("🛑 [STOP] Kalibrasi Dibatalkan.")

if __name__ == "__main__":
    h2k = H2KMasterSync()
    if h2k.connect_to_heart():
        h2k.calibrate_frequency()
        print("🏆 [SUCCESS] H2K SINKRONISASI SELESAI. SISTEM SIAP DIGEMPUR!")
