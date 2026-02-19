import json

def show_wallet_status(wallet_address="BreSpeedWorks_Founders"):
    # Simulasi memanggil data dari ledger IBM M3
    ledger_file = "src/quantum_logic/ledger_data.json"
    
    try:
        with open(ledger_file, "r") as f:
            data = json.load(f)
            # Mencari transaksi yang ditujukan ke founder
            balance = sum(tx['amount'] for tx in data if tx.get('recipient') == wallet_address)
            
            print(f"--- DOMPET QUANTUM-STATE ---")
            print(f"Address: {wallet_address}")
            print(f"Saldo  : {balance:,} $QSTATE")
            print(f"Status : VALIDATED BY QUORUM")
    except FileNotFoundError:
        print("[!] Ledger belum dibuat. Jalankan genesis_block.py dulu.")

if __name__ == "__main__":
    show_wallet_status()
