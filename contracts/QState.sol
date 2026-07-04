// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QuorumStateToken is ERC20, Ownable {
    // Batas Maksimal Suplai: 1.000 Triliun (1.000T)
    uint256 public constant MAX_SUPPLY = 1000000000000000 * 10**18;

    constructor() ERC20("Quorum State Token", "QSTATE") Ownable(msg.sender) {
        // TAHAP 1: Langsung cetak 1 Triliun (1T) saat peluncuran
        _mint(msg.sender, 1000000000000 * 10**18);
    }

    // FUNGSI UNTUK TAHAP 2, 3, dan 4
    // Hanya Anda (Owner) yang bisa memanggil fungsi ini
    function mintNextPhase(address to, uint256 amountInTrillions) public onlyOwner {
        uint256 amountToMint = amountInTrillions * 1000000000000 * 10**18;
        require(totalSupply() + amountToMint <= MAX_SUPPLY, "Melebihi batas maksimal 1000T!");
        _mint(to, amountToMint);
    }
}
