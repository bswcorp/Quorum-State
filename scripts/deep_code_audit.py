import os
import re

def audit_supply_integrity(directory):
    print("🔍 [AUDIT] Memulai Deep Scan pada Folder Scripts...")
    target_supply = "1000000000000" # 1 Triliun
    error_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    
                    # 1. Cek Konsistensi Angka Suplai
                    if "supply" in content.lower() and target_supply not in content:
                        print(f"❌ [WARNING] Ketidaksesuaian Suplai di: {file}")
                        error_count += 1
                    
                    # 2. Cek Celah Keamanan Dasar (Hardcoded Passwords)
                    if re.search(r"password\s*=\s*['\"].*['\"]", content, re.IGNORECASE):
                        print(f"⚠️ [SECURITY] Hardcoded Password terdeteksi di: {file}")
                        error_count += 1

                    # 3. Cek Implementasi NIST (Kyber/Dilithium)
                    if "nist" not in content.lower():
                        print(f"💡 [INFO] File {file} belum mencantumkan referensi NIST PQC.")

    print(f"\n✅ [RESULT] Audit Selesai. Total Temuan Kritis: {error_count}")
    if error_count == 0:
        print("🚀 STATUS: 1T $QSTATE READY FOR GLOBAL DEPLOYMENT!")

if __name__ == "__main__":
    # Pastikan menjalankan dari root folder project
    audit_supply_integrity("scripts")
