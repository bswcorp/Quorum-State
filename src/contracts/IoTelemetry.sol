// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title IoTelemetry $QSTATE
 * @dev Kontrak untuk enkapsulasi data sensor IoT & Robotika ke Ledger.
 */
contract IoTelemetry {
    address public owner;

    struct TelemetryData {
        uint256 timestamp;
        string deviceId;
        string sensorPayload; // Contoh: {"temp": 25, "batt": 88, "pos": "x10y20"}
        bytes32 dataHash;     // Bukti integritas data (NIST Standard)
    }

    // Mapping dari ID Perangkat ke riwayat data mereka
    mapping(string => TelemetryData[]) private deviceHistory;

    event DataSealed(string indexed deviceId, uint256 timestamp, bytes32 dataHash);

    modifier onlyOwner() {
        require(msg.sender == owner, "Hanya Capo/Owner yang bisa akses!");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Menyegel data telemetri ke blockchain.
     */
    function sealData(string memory _deviceId, string memory _payload) public onlyOwner {
        bytes32 _hash = keccak256(abi.encodePacked(_payload, block.timestamp));
        
        TelemetryData memory newData = TelemetryData({
            timestamp: block.timestamp,
            deviceId: _deviceId,
            sensorPayload: _payload,
            dataHash: _hash
        });

        deviceHistory[_deviceId].push(newData);
        emit DataSealed(_deviceId, block.timestamp, _hash);
    }

    /**
     * @dev Mengambil total catatan untuk satu perangkat.
     */
    def getLogCount(string memory _deviceId) public view returns (uint256) {
        return deviceHistory[_deviceId].length;
    }
}
