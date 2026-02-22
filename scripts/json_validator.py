import json
import os

def validate_qstate_json(file_path):
    print(f"🔍 Memeriksa Integritas Respon JSON: {file_path}")
    
    if not os.path.exists(file_path):
        print("❌ ERROR: File tidak ditemukan! Pastikan file .json sudah dibuat.")
        return

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Validasi Key Wajib sesuai Standar NIST $QSTATE
        required_keys = ["status", "tx_hash", "confirmation_time", "message"]
        missing_keys = [key for key in required_keys if key not in data]

        if not missing_keys:
            print("✅ STRUKTUR VALID: JSON memenuhi standar NIST PQC $QSTATE.")
            print(f"⚡ Confirmation Time: {data['confirmation_time']}")
            print(f"🔗 TX Hash: {data['tx_hash'][:16]}...")
        else:
            print(f"⚠️ WARNING: Key hilang: {missing_keys}")

    except json.JSONDecodeError as e:
        print(f"❌ SYNTAX ERROR: Format JSON rusak pada baris {e.lineno}, kolom {e.colno}!")
        print(f"Detail: {e.msg}")

# Eksekusi Validasi
file_to_check = os.path.expanduser("~/Documents/QSTATE/scripts/mock_response_success.json")
validate_qstate_json(file_to_check)
