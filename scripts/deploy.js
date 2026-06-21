const hrd = require("hardhat");

async function main() {
  const [deployer] = await hrd.ethers.getSigners();
  console.log("Memulai Migrasi dengan Wallet Developer:", deployer.address);

  // Alamat Token Dummy/Asli & Alamat Korporat Penerima Manfaat
  const TOKEN_ALAMAT = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0"; 
  const PENERIMA_MANFAAT = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
  const WAKTU_MULAI = Math.floor(Date.now() / 1000);
  const TOTAL_ALOKASI = hrd.ethers.parseEther("150000000"); // 150 Juta Token SPOV

  const SSPAContract = await hrd.ethers.getContractFactory("SSPAEnterpriseTokenVesting");
  const sspaVesting = await SSPAContract.deploy(TOKEN_ALAMAT, PENERIMA_MANFAAT, WAKTU_MULAI, TOTAL_ALOKASI);

  await sspaVesting.waitForDeployment();
  console.log("SSPA Enterprise Vesting Sukses Mendarat di Alamat:", await sspaVesting.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
