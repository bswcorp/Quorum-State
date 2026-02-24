import requests
import base64
import json
import time

# --- KONFIGURASI KEDAULATAN ---
GITHUB_TOKEN = "GANTI_DENGAN_TOKEN_ANDA"
REPO_OWNER = "bswcorp"
REPO_NAME = "Quorum-State"
FILE_PATH = "docs/finance/treasury_data.json"
BRANCH = "main"

def update_github_json(new_entry):
    url = f"https://api.github.com{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

    # 1. Ambil File Lama (Dapatkan SHA-nya)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_data = response.json()
        sha = file_data['sha']
        content = base64.b64decode(file_data['content']).decode('utf-8')
        data_list = json.loads(content)
    else:
        print("❌ Gagal mengambil data lama!"); return

    # 2. Tambahkan Data Baru (Pajak BIZ/ENT atau Beasiswa EDU)
    data_list.append(new_entry)
    updated_content = json.dumps(data_list, indent=2)
    encoded_content = base64.b64encode(updated_content.encode('utf-8')).decode('utf-8')

    # 3. Push Update ke GitHub
    payload = {
        "message": f"Finance: Auto-update Treasury Log {time.strftime('%Y-%m-%d')}",
        "content": encoded_content,
        "sha": sha,
        "branch": BRANCH
    }
    
    put_response = requests.put(url, headers=headers, json=payload)
    if put_response.status_code == 200:
        print("✅ [SUCCESS] Dashboard Transparansi Terupdate Secara Real-Time!")
    else:
        print(f"❌ Error Update: {put_response.json()}")

# --- SIMULASI INPUT DATA BARU ---
entry_baru = {
    "date": time.strftime("%Y-%m-%d"),
    "desc": "Penerimaan Pajak QST-ENT (Infrastructure Fund)",
    "type": "IN",
    "amount": 5000000,
    "status": "NIST-VERIFIED"
}

update_github_json(entry_baru)
