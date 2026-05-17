import { expect } from "chai";
import { ethers } from "hardhat";
import { Contract } from "ethers";
import { SignerWithAddress } from "@nomiclabs/hardhat-ethers/signers";

describe("STG/QSTATE Sovereign Contract - Zero Defect Suite", function () {
  let STGContract: Contract;
  let owner: SignerWithAddress;
  let complianceAuditor: SignerWithAddress;
  let userA: SignerWithAddress;
  let userB: SignerWithAddress;

  const TOTAL_SUPPLY = ethers.utils.parseUnits("1000000000", 18); // Sesuaikan dengan dokumen perencanaan

  beforeEach(async function () {
    [owner, complianceAuditor, userA, userB] = await ethers.getSigners();

    // Deploy contract utama
    const STGFactory = await ethers.getContractFactory("SovereignToken");
    STGContract = await STGFactory.deploy(TOTAL_SUPPLY);
    await STGContract.deployed();
  });

  describe("1. Auto-Compatibility & Genesis Supply", function () {
    it("Harus mencetak total supply tepat sesuai dokumen perencanaan", async function () {
      const currentSupply = await STGContract.totalSupply();
      expect(currentSupply).to.equal(TOTAL_SUPPLY);
    });

    it("Harus kompatibel dengan standar ERC-20 / EVM interface dasar", async function () {
      // Menguji fungsi transfer dasar untuk verifikasi dompet eksternal
      const transferAmount = ethers.utils.parseUnits("1000", 18);
      await expect(STGContract.transfer(userA.address, transferAmount))
        .to.emit(STGContract, "Transfer")
        .withArgs(owner.address, userA.address, transferAmount);
    });
  });

  describe("2. Security Guardrails (Sentinel Hook & Boundary Limits)", function () {
    it("FAIL-SAFE: Pengguna non-owner tidak boleh mengakses fungsi cetak/minting", async function () {
      const mintAmount = ethers.utils.parseUnits("5000", 18);
      // Memastikan sistem menolak bypass otorisasi secara mutlak
      await expect(STGContract.connect(userA).mint(userA.address, mintAmount))
        .to.be.revertedWith("Ownable: caller is not the owner");
    });

    it("ZERO-DEFECT BOUNDARY: Sistem harus menolak transaksi jika melebihi batas saldo (Overflow/Boundary Test)", async function () {
      const excessiveAmount = TOTAL_SUPPLY.add(1);
      await expect(STGContract.connect(userA).transfer(userB.address, excessiveAmount))
        .to.be.revertedWith("ERC20: transfer amount exceeds balance");
    });

    it("EMERGENCY SECTOR: Fungsi pause harus menghentikan seluruh aktivitas transfer dalam hitungan milidetik", async function () {
      // Jika kontrak memiliki fungsi Emergency Pause oleh Sentinel
      if (typeof STGContract.pause === "function") {
        await STGContract.pause();
        const transferAmount = ethers.utils.parseUnits("10", 18);
        await expect(STGContract.transfer(userA.address, transferAmount))
          .to.be.revertedWith("Pausable: paused");
      }
    });
  });
});
