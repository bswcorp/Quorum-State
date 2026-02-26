
#!/bin/bash
# 💎 THE BIRTH OF 1T $QSTATE: GENESIS CREATION
# Memastikan Hyperledger mengenali kedaulatan Bintaro.

export PATH=$PATH:~/fabric-samples/bin
export FABRIC_CFG_PATH=$PWD

echo "🌟 [GENESIS] Menciptakan Blok #0 di Node 01 Bintaro..."

configtxgen -profile QStateGenesis -channelID system-channel -outputBlock ./system-genesis.block

if [ $? -eq 0 ]; then
    echo "✅ [SUCCESS] system-genesis.block BERHASIL DICIPTAKAN!"
    echo "🔒 [STATUS] 1 Triliun Kedaulatan Terkunci dalam Hash Kriptografi."
else
    echo "❌ [FAILED] Terjadi gangguan pada transmisi Roh Fisika!"
fi
