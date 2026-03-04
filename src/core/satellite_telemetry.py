import random
import time
from datetime import datetime

class SatelliteTelemetry:
    def __init__(self):
        self.sat_id = "QS-SAT-01 (WIZARD-EYE)"
        self.base_coords = {"lat": -6.2, "lon": 106.8} # Start di atas langit Jakarta/Ciracas

    def get_live_data(self):
        """Menghasilkan data pergerakan satelit real-time di orbit LEO"""
        now = datetime.now().strftime("%H:%M:%S")
        # Simulasi pergerakan orbit kecepatan 27,000 km/jam
        lat = self.base_coords["lat"] + (random.uniform(-0.1, 0.1))
        lon = self.base_coords["lon"] + (random.uniform(-0.1, 0.1))
        
        return {
            "timestamp": now,
            "sat_id": self.sat_id,
            "coords": f"{lat:.4f}, {lon:.4f}",
            "altitude": f"{random.randint(540, 560)} KM",
            "signal": "STRONG (GHOST-UPLINK)",
            "status": "KENDALI-ACTIVE"
        }

