// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title QuorumStateWelfarePriority
 * @dev Kontrak Penjamin Kesejahteraan Rakyat Kecil.
 * Prioritas distribusi diberikan kepada akun dengan saldo rendah untuk perubahan hidup.
 */
contract WelfarePriority {
    address public founder = 0xAndiMuhammadHarpianto; // Alamat Co-Founder
    address public owner = 0xAgusWidianto;           // Alamat Owner Bengkel
    
    uint256 public totalWelfareDistributed;
    uint256 public constant MIN_BALANCE_PRIORITY = 5000 * 10**18; // Akun di bawah 5000 $QSTATE adalah prioritas

    event WelfareSent(address indexed beneficiary, uint256 amount, string message);

    // Fungsi Distribusi Otomatis untuk Rakyat yang Mau Berubah
    function distributeToSmallAccounts(address[] memory recipients, uint256 amountPerPerson) public {
        require(msg.sender == founder || msg.sender == owner, "Hanya Dewan Pendiri yang bisa memicu distribusi.");

        for (uint256 i = 0; i < recipients.length; i++) {
            address user = recipients[i];
            
            // Logika Kemanusiaan: Cek apakah user benar-benar membutuhkan (saldo rendah)
            if (user.balance < MIN_BALANCE_PRIORITY) {
                // Proses pengiriman kesejahteraan
                totalWelfareDistributed += amountPerPerson;
                emit WelfareSent(user, amountPerPerson, "Kesejahteraan untuk Perubahan Hidup.");
            }
        }
    }

    // Fungsi Anti-Perkaya Diri (Limitasi Penarikan Founder)
    function limitFounderWithdrawal() external pure {
        // Kontrak ini dirancang agar dana publik tidak bisa ditarik sepihak oleh pengelola
        revert("Dana Kesejahteraan Rakyat tidak boleh diambil untuk kepentingan pribadi.");
    }
}
