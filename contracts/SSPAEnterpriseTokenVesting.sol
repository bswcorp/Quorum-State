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
     * @dev Menghitung jumlah akumulasi token yang seharusnya sudah tidak terkunci berdasarkan waktu.
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
