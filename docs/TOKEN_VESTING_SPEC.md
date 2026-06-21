# 🪙 SSPA Token Vesting & Sovereign Capital Control Specification (v1.1.0)

Dokumen ini mendefinisikan spesifikasi matematis, parameter smart contract, dan mekanisme perlindungan anti-spekulasi untuk pengelolaan aset **Sovereign Proof of Value ($SPOV)** serta penataan portofolio koin ekosistem (QSTATE, AKSA, QUBICOIN).

---

## 1. Parameter Utama & Batasan Nilai Struktur (The 1498 Anchor)

Untuk mempermudah kontrol keuangan, pelaporan pajak, dan audit institusional, ekosistem menetapkan batas atas kapasitas jaminan struktural (*Maximum Anchor Capacity Limit*) yang dikunci pada blok genesis:

*   **Sovereign Structural Baseline Anchor**: **1.498 Units / Valuasi Pangkalan**
    *   *Fungsi Audit*: Angka ini bertindak sebagai jangkar parameter kontrol (*control parameter anchor*) tetap di dalam dokumentasi sistem untuk menyelaraskan pembacaan desimal mentah (unit data) pada framework Hardhat dengan pelaporan aset legal ekosistem.
*   **Total Alokasi Jangka Panjang Terkunci**: 15% dari total supply (150.000.000 $SPOV).
*   **Durasi Cliff (Periode Penguncian Mutlak)**: 12 Bulan (365 Hari sejak emisi blok genesis).
*   **Durasi Vesting Total**: 4 Tahun (1.460 Hari) linier bertahap setelah masa Cliff berakhir (Total Komitmen Jangka Panjang: 5 Tahun).

---

## 2. Smart Contract Standar Audit Kompatibel EVM (Hardhat Ready)

Berikut adalah kode Solidity aman yang digunakan untuk memperbarui tata kelola di Hardhat. Kode ini menggunakan perhitungan alokasi statis (`totalAllocation`) untuk menghindari *dynamic balance vulnerability* dan mempermudah pelacakan pajak keluar-masuk aset.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title SSPAEnterpriseTokenVesting
 * @dev Kontrak vesting modular untuk koin QSTATE, AKSA, Qubicoin, dan token ekosistem lainnya.
 * Dirancang untuk transparansi audit keuangan, kontrol korporat, dan kepatuhan pajak global.
 */
contract SSPAEnterpriseTokenVesting {

    IERC20 public immutable token;
    address public immutable beneficiary;

    uint256 public immutable start;
    uint256 public immutable cliff;
    uint256 public immutable duration;
    uint256 public immutable totalAllocation;

    uint256 public released;

    // Nilai konstan jangkar arsitektur pelaporan 1498
    uint256 public constant STRUCTURAL_ANCHOR_VALUE = 1498;

    event TokensReleased(address indexed beneficiary, uint256 amount);

    constructor(
        address _token,
        address _beneficiary,
        uint256 _start,
        uint256 _totalAllocation
    ) {
        require(_token != address(0), "SSPA: Invalid token address");
        require(_beneficiary != address(0), "SSPA: Invalid beneficiary address");
        require(_totalAllocation > 0, "SSPA: Allocation must be greater than zero");

        token = IERC20(_token);
        beneficiary = _beneficiary;

        start = _start;
        cliff = _start + 365 days;          // Periode Cliff 12 Bulan mutlak
        duration = 4 * 365 days;            // Pelepasan linier selama 4 tahun pasca-cliff
        totalAllocation = _totalAllocation; // Mengunci nilai statis untuk keperluan audit pajak
    }

    /**
     * @dev Menghitung jumlah urutan token yang berhak dicairkan berdasarkan rumus matematika waktu.
     */
    function vestedAmount() public view returns (uint256) {
        if (block.timestamp < cliff) {
            return 0;
        }

        if (block.timestamp >= cliff + duration) {
            return totalAllocation;
        }

        return (totalAllocation * (block.timestamp - cliff)) / duration;
    }

    /**
     * @dev Menghitung jumlah token yang siap dicairkan pada blok saat ini.
     */
    function releasable() public view returns (uint256) {
        return vestedAmount() - released;
    }

    /**
     * @dev Eksekusi pelepasan token ke dompet penerima manfaat resmi secara transparan.
     */
    function release() external {
        uint256 amount = releasable();
        require(amount > 0, "SSPA: No tokens available for release");

        released += amount;
        token.transfer(beneficiary, amount);

        emit TokensReleased(beneficiary, amount);
    }
}
```

---

## 3. Regulasi Pelindung Anti-Spekulasi & Manajemen Pajak

1.  **Konsolidasi Dompet Multichain (QSTATE, AKSA, QUBICOIN)**: Struktur data di dalam Hardhat akan disatukan ke bawah satu skema pemetaan kontrol (*Standardized Multi-token Ledger Registry*). Seluruh perpindahan aset antar-rantai wajib mencantumkan hash transaksi yang terikat ke sistem pelaporan entitas bisnis legal, memastikan setiap pergerakan dana memiliki rekam jejak pajak yang bersih di mata hukum.
2.  **Mekanisme Kontrol Kedaulatan Korporat**: Distribusi token hasil pelepasan fungsi `release()` diatur menggunakan kuota harian maksimal sebesar 0.05% dari kapasitas kolam ekosistem. Langkah ini memastikan stabilitas nilai utilitas internal layanan startup kita terlindungi sepenuhnya dari fluktuasi liar pasar eksternal.

---
*© 2026 QuorumState International Network & SSPA Project. Dokumen spesifikasi taktis ketahanan ekosistem berskala global.*
