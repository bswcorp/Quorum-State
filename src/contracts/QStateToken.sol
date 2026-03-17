// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./GlobalSovereignty.sol";

contract QStateToken is ERC20 {
    // Total Suplai: 1.000.000.000 (1 Miliar) $QSTATE
    uint256 private constant INITIAL_SUPPLY = 1000000000 * 10**18;
    address public owner;

    constructor() ERC20("Quorum State Token", "QSTATE") {
        owner = msg.sender;
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Fungsi untuk cek kedaulatan sebelum transaksi besar (opsional)
    function transferSovereign(address to, uint256 amount) public returns (bool) {
        // Logika kedaulatan bisa ditambahkan di sini
        return transfer(to, amount);
    }
}
