// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title QSTATE Investor Vesting Escrow
 * @dev Mengunci 10% koin & melepaskannya secara otomatis setiap bulan selama 12 bulan.
 */
contract QStateVesting {
    address public founder; // Andi Muhammad Harpianto
    uint256 public constant VESTING_PERIOD = 12; // 12 Bulan

    struct Grant {
        uint256 totalAmount;
        uint256 amountReleased;
        uint256 startTime;
        uint256 lastReleaseDate;
        uint8 releaseDay; // Tanggal kesepakatan (misal: tanggal 5)
    }

    mapping(address => Grant) public grants;

    constructor() {
        founder = msg.sender;
    }

    // Mendaftarkan Investor & Menentukan Tanggal Cair (Release Day)
    function addInvestor(address _investor, uint256 _amount, uint8 _day) external {
        require(msg.sender == founder, "Hanya Founder");
        require(_day >= 1 && _day <= 28, "Tanggal 1-28 untuk keamanan");
        
        grants[_investor] = Grant({
            totalAmount: _amount,
            amountReleased: 0,
            startTime: block.timestamp,
            lastReleaseDate: 0,
            releaseDay: _day
        });
    }

    // Fungsi Cair Otomatis (Dijalankan per bulan)
    function releaseMonthly() external {
        Grant storage grant = grants[msg.sender];
        require(grant.totalAmount > 0, "Bukan Investor");
        
        uint256 monthlyAmount = grant.totalAmount / VESTING_PERIOD;
        // Logika: Cek apakah sudah masuk bulan berikutnya & sesuai tanggal kesepakatan
        // ... (Logika Timestamp Blockchain)
        
        grant.amountReleased += monthlyAmount;
        // Kirim Koin ke Dompet Investor
    }
}
