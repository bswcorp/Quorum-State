// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QStateToken is ERC20, Ownable {
    // Batas Maksimal: 1.000 Triliun (1.000T)
    uint256 public constant MAX_SUPPLY = 1000000000000000 * 10**18;

    constructor() ERC20("Quorum State Token", "QSTATE") Ownable(msg.sender) {
        // Tahap 1: Cetak 1T di awal
        _mint(msg.sender, 1000000000000 * 10**18);
    }

    // Fungsi untuk mencetak tahap berikutnya (2, 3, dan 4)
    function mintNextPhase(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Melebihi batas maksimal 1000T!");
        _mint(to, amount);
    }
}
