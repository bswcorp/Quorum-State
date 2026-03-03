import random
import time

class QStateIncentive:
    def __init__(self, core_system):
        self.core = core_system
        self.reward_amount = 1000  # Piala GenAtoZmate
        self.penalty_ratio = 0.5   # Slashing 50% aset (GenAtoZmad)
        self.trust_matrix = {}      # Skor reputasi per node

    def evaluate_node(self, node_address, is_honest):
        """
        Menilai perilaku node: Reward untuk kejujuran, Slashing untuk kecurangan.
        """
        if node_address not in self.trust_matrix:
            self.trust_matrix[node_address] = 100 # Skor awal

        if is_honest:
            # Berikan Reward (GenAtoZmate)
            self.core.mint(node_address, self.reward_amount)
            self.trust_matrix[node_address] += 5
            print(f"[REWARD] {node_address}: +{self.reward_amount} $QSTATE (GenAtoZmate)")
        else:
            # Eksekusi Slashing (GenAtoZmad - Sebelum Subuh)
            current_balance = self.core.get_balance(node_address)
            slashed_amount = current_balance * self.penalty_ratio
            self.core.ledger[node_address] -= slashed_amount
            self.trust_matrix[node_address] -= 50
            print(f"[PUNISH] {node_address}: -{slashed_amount} $QSTATE (GenAtoZmad/Slashed)")
            
            if self.trust_matrix[node_address] < 10:
                print(f"[ALERT] {node_address} Dikeluarkan dari Quorum 676!")

    def run_simulation(self, rounds=5):
        """Menjalankan simulasi beberapa putaran transaksi"""
        nodes = ["NODE-JUJUR-1", "NODE-CURANG-X", "NODE-JUJUR-2"]
        for node in nodes:
            self.core.mint(node, 10000) # Saldo awal

        for i in range(rounds):
            print(f"\n--- Putaran Simulasi Ke-{i+1} ---")
            for node in nodes:
                # Simulasi: Node-Curang-X akan berbuat curang di putaran genap
                behavior = False if "CURANG" in node and i % 2 == 0 else True
                self.evaluate_node(node, behavior)
            time.sleep(1)

# Inisialisasi dari Core utama
if __name__ == "__main__":
    from qstate_core import QuorumStateCore
    qs_core = QuorumStateCore()
    incentive = QStateIncentive(qs_core)
    incentive.run_simulation()
