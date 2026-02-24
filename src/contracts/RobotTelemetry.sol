// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RobotTelemetry {
    struct Log {
        uint256 timestamp;
        string sensorData; // Contoh: "x:1.2, y:0.5, battery:88%"
    }
    
    mapping(string => Log[]) public robotLogs;

    function recordTelemetry(string memory _robotId, string memory _data) public {
        robotLogs[_robotId].push(Log(block.timestamp, _data));
    }
}
