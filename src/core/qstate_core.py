    def check_gatekeeper_protocol(self, partner_address, commitment_pct):
        """
        Protokol Kuda-Kuda: Mengunci akses hanya bagi mitra dengan komitmen 10%.
        Mencegah infiltrasi aset tanpa kesepakatan resmi.
        """
        MINIMUM_COMMITMENT = 10 # Standar 10% dari Godfather
        
        if commitment_pct >= MINIMUM_COMMITMENT:
            print(f"[ACCESS GRANTED] Mitra {partner_address} terverifikasi.")
            return True
        else:
            print(f"[ACCESS DENIED] Komitmen di bawah 10%. Pasang kuda-kuda!")
            return False
            
