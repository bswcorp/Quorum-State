  class QuorumContract:
    """Simulasi Smart Contract berbasis IPO di jaringan Quorum-State."""
    def __init__(self, contract_name, total_shares):
        self.name = contract_name
        self.shares = total_shares
        self.holders = {}
        self.is_executed = False

    def invest(self, investor_address, amount):
        if amount <= self.shares:
            self.holders[investor_address] = amount
            self.shares -= amount
            return f"Investasi berhasil: {amount} saham dialokasikan."
        return "Saham tidak mencukupi."

    def execute_quorum_call(self, computors_votes):
        """Hanya dieksekusi jika mencapai kuorum (2/3 dari 676 = 451 suara)."""
        if computors_votes >= 451:
            self.is_executed = True
            return "KONTRAK DIEKSEKUSI: Kuorum Tercapai."
        return "GAGAL: Kuorum Tidak Tercapai."

# Testing Contract
if __name__ == "__main__":
    contract = QuorumContract("AI-Inference-IPO", 1000)
    print(contract.invest("BreSpeedWorks_Wallet", 500))
    print(contract.execute_quorum_call(500)) # Simulasi suara computors
