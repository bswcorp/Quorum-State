Arsitektur Dompet Kedaulatan ($QSTATE)
1. Komponen Utama (The Anatomy)
Identity (Jasad): Menggunakan h2k_biological_engine.py. Kunci privat tidak disimpan sebagai file biasa, tapi diturunkan dari hash detak jantung Capo.
Ledger (Buku Besar): Hyperledger Fabric Local Instance di Node 01 Bintaro.
Interface (Wajah): Dashboard berbasis Web Lokal (HTML/JS) yang berjalan di jaringan Air-Gapped Bintaro.
2. Alur Transaksi (The Flow)
Auth: User menempelkan sensor H2K (atau input Bio-Signature).
Sign: Sistem mengambil Private Key dari memori sementara (RAM), menandatangani transaksi, lalu menghapus kunci tersebut seketika.
Broadcast: Transaksi dikirim ke Node 01 (IBM M2/M3) untuk dicatat dalam blok.
Confirm: Saldo ter-update di buku besar dalam < 1 detik (Tanpa biaya Gas/Bensin
