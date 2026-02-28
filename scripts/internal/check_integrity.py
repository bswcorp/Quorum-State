import os

# 🐍 SENTINEL INTEGRITY CHECKER v2.1.3
files_to_check = [
    "docs/legal/INTERNAL_FOUNDERS_AGREEMENT_GALAXY.md",
    "docs/tech/Q_LINK_SOVEREIGN_INTERNET.md",
    "docs/legal/VOLUNTEER_AGREEMENT_QLINK.md",
    "scripts/internal/sentinel_sovereign_monitor.py"
]

def verify_vault():
    print("🔍 [SENTINEL] Memeriksa kelengkapan administrasi kedaulatan...")
    for f in files_to_check:
        if os.path.exists(f):
            print(f"✅ [FOUND] {f}")
        else:
            print(f"❌ [MISSING] {f} - CEO, HUBUNGI CDxaiO SEGERA!")

if __name__ == "__main__":
    verify_vault()
