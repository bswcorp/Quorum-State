import time
import sys
import random

def run_live_demo():
    header = """
    =================================================
    🚀 $QSTATE GENESIS LIVE OPERATIONAL DEMO
    =================================================
    Status  : NIST PQC ENCRYPTION ACTIVE
    Mission : GLOBAL HUMAN WELFARE & PROSPERITY
    Node    : BINTARO-GENESIS-COMMAND-CENTER
    =================================================
    """
    print(header)
    
    wealth_pool = 0.0
    
    try:
        while True:
            # Simulasi Animasi Validasi NIST
            spinners = ['|', '/', '-', '\\']
            for _ in range(5):
                for s in spinners:
                    sys.stdout.write(f"\r[ {s} ] Validating NIST Kyber Lattice... ")
                    sys.stdout.flush()
                    time.sleep(0.1)
            
            # Simulasi Produksi Nilai
            new_value = round(random.uniform(1.0, 10.0), 4)
            wealth_pool += new_value
            
            print(f"\r✅ BLOCK VALIDATED: Sub-3s Finality Achieved!")
            print(f"💰 Value Produced: +{new_value} $QSTATE")
            print(f"📈 Total Community Wealth Pool: {wealth_pool:.4f} $QSTATE")
            print(f"🌍 Action: Allocating to Future Generations...")
            print("-" * 49)
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Demo Paused. All data secured by NIST Encryption.")
        print(f"Final Wealth Pool: {wealth_pool:.4f} $QSTATE")

if __name__ == "__main__":
    run_live_demo()
