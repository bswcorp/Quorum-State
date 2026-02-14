# Quorum-State ($QSTATE) Whitepaper
## Bab 2: Arsitektur Kriptografi Pasca-Kuantum (PQC)

### 2.1 Enkripsi Berbasis Kisi (Lattice-Based Cryptography)
Untuk memitigasi risiko algoritma Shor yang dapat memecahkan ECDSA (Elliptic Curve Digital Signature Algorithm), Quorum-State mengadopsi skema **Lattice-based Cryptography**. Kami mengintegrasikan standar NIST terbaru:
- **CRYSTALS-Dilithium:** Digunakan untuk tanda tangan digital transaksi guna memastikan integritas pengirim.
- **CRYSTALS-Kyber:** Digunakan untuk mekanisme enkripsi data sensitif dalam jaringan.

### 2.2 Algoritma Hashing K12 (Keccak-256 Speed)
Kecepatan adalah identitas kami. Quorum-State tetap menggunakan varian **K12 (Keccak-12)** untuk proses hashing. 
- **Efisiensi:** K12 dirancang untuk eksekusi paralel yang sangat cepat, mendukung target 15,5 juta TPS.
- **Resistensi Kuantum:** Secara inheren, hashing kriptografi seperti K12 lebih tahan terhadap algoritma Grover dibandingkan algoritma asimetris terhadap algoritma Shor.

### 2.3 Teorema No-Cloning dalam Validasi
Dalam protokol Quorum-State, status "Superposisi" transaksi tidak dapat disalin (cloning) oleh pihak ketiga tanpa mengubah status aslinya. Hal ini menciptakan lapisan keamanan fisik yang mencegah serangan *double spending* pada tingkat kuantum.

### 2.4 Mekanisme Quorum 676 Computors
Validasi tetap dilakukan oleh 676 node terpilih. Namun, setiap node diwajibkan menjalankan modul **PQC-Validator** yang memverifikasi tanda tangan Dilithium sebelum transaksi masuk ke dalam status superposisi untuk diproses.
