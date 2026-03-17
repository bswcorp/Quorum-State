from web3 import Web3
import json

# Hubungkan ke jaringan (Gunakan RPC Testnet seperti Sepolia atau Polygon Mumbai)
rpc_url = "ISI_DENGAN_RPC_URL_ANDA" 
web3 = Web3(Web3.HTTPProvider(rpc_url))

def deploy_token():
    # Pastikan Anda sudah mengompilasi kontrak dan memiliki ABI serta Bytecode
    abi = [...] # Tempel ABI dari kompilasi
    bytecode = "0x..." # Tempel Bytecode

    account = "ALAMAT_WALLET_ANDA"
    private_key = "PRIVATE_KEY_ANDA"

    QState = web3.eth.contract(abi=abi, bytecode=bytecode)
    
    # Kirim transaksi deploy
    tx = QState.constructor().build_transaction({
        'from': account,
        'nonce': web3.eth.get_transaction_count(account),
        'gas': 3000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f"Koin $QSTATE Sedang Mengudara! Hash: {tx_hash.hex()}")

if __name__ == "__main__":
    deploy_token()
  
