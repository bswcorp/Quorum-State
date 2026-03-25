// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

contract QStateTreasury {
    IERC20 public qstateToken;
    address public stgGovernance;

    event FundingReleased(address recipient, uint256 amount, string projectScale);

    constructor(address _qstateToken, address _governance) {
        qstateToken = IERC20(_qstateToken);
        stgGovernance = _governance;
    }

    // Fungsi pendanaan otomatis berdasarkan skala proyek
    function releaseFunding(
        address _projectAddress, 
        uint256 _amount, 
        string memory _scale // "NANO", "KECIL", "MENENGAH", "BESAR"
    ) external {
        require(msg.sender == stgGovernance, "Hanya melalui Quorum-State");
        
        qstateToken.transfer(_projectAddress, _amount);
        emit FundingReleased(_projectAddress, _amount, _scale);
    }
}
