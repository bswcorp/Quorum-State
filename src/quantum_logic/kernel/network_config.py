import uuid
import socket

class NetworkConfig:
    """Identitas Unik Node Quorum-State v3.0.0"""
    def __init__(self):
        self.version = "v3.0.0"
        self.node_id = str(uuid.uuid4())[:8] # ID Unik 8 Karakter
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.port = 676 # Port Standar Quorum

    def get_identity(self):
        return {
            "node_id": self.node_id,
            "ip_address": self.local_ip,
            "protocol": f"H2K-Bridge-{self.version}",
            "status": "AUTHORIZED"
        }

if __name__ == "__main__":
    config = NetworkConfig()
    print(f"--- Identitas Node Quorum-State ---")
    print(config.get_identity())
