import time
import random

class TickListener:
    """
    Simulasi pemantauan data (Tick) dari jaringan Qubic.
    Data yang masuk akan langsung dibungkus oleh Legacy Bridge.
    """
    def __init__(self):
        self.is_listening = False
        self.total_ticks_captured = 0

    def start_listening(self):
        print("--- QUORUM-STATE TICK LISTENER ONLINE ---")
        print("[*] Menghubungkan ke port komunikasi Qubic (Legacy)...")
        self.is_listening = True
        
        try:
            while self.is_listening:
                # Simulasi menangkap data Tick eksternal
                current_tick = random.randint(1000000, 9999999)
                print(f"[📡] Tick Tertangkap: #{current_tick} | Status: Sinkronisasi...")
                
                self.total_ticks_captured += 1
                # Jeda simulasi antar Tick
                time.sleep(2) 
                
        except KeyboardInterrupt:
            self.stop_listening()

    def stop_listening(self):
        self.is_listening = False
        print(f"\n--- LISTENER OFFLINE ---")
        print(f"Total Tick yang tercatat: {self.total_ticks_captured}")

if __name__ == "__main__":
    listener = TickListener()
    listener.start_listening()
