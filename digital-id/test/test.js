const DigitalIdentityCard = artifacts.require("DigitalIdentityCard");

contract("DigitalIdentityCard", (accounts) => {
  let digitalIdentityCardInstance;

  before(async () => {
    digitalIdentityCardInstance = await DigitalIdentityCard.deployed();
  });

  it("should create a sample digital identification card", async () => {
    const name = "John Doe";
    const birthday = 946684800; // January 1, 2000 (Unix timestamp)
    const driversLicenseNumber = 123456789;

    // Create the digital identification card
    await digitalIdentityCardInstance.createIdentity(name, birthday, driversLicenseNumber, { from: accounts[0] });

    // Retrieve the created identity
    const identity = await digitalIdentityCardInstance.getIdentity(accounts[0]);

    // Verify the created identity matches the expected values
    assert.equal(identity[0], name, "Name does not match");
    assert.equal(identity[1], birthday, "Birthday does not match");
    assert.equal(identity[2], driversLicenseNumber, "Driver's license number does not match");
  });
});
