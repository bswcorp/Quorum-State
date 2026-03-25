// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SultanSmartMeter {
    struct MeterNode {
        string aksaraID;
        address familyWallet;
        uint256 dailyQuota;    // Kuota energi gratis (kWh)
        uint256 currentUsage;
        bool isActive;
    }

    mapping(string => MeterNode) public nodes;
    
    // Fungsi: Alokasi Energi Sultan (Subsidi 111%)
    function allocateEnergy(string memory _aksaraID, uint256 _quota) external {
        require(msg.sender == governanceAddress, "Hanya Otoritas STG");
        nodes[_aksaraID].dailyQuota = (_quota * 111) / 100; // Formula Sultan +11%
        nodes[_aksaraID].isActive = true;
    }

    // Fungsi: Pelaporan Otomatis (No Human Intervention)
    function reportUsage(string memory _aksaraID, uint256 _usage) external {
        // Validasi otomatis dari sensor hardware
        nodes[_aksaraID].currentUsage += _usage;
    }
}
