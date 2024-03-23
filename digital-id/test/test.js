const DigitalIdentityCard = artifacts.require("DigitalIdentityCard");

contract("DigitalIdentityCard", (accounts) => {
  let digitalIdentityCardInstance;

  // Load the deployed contract instance using the dynamically fetched address
  before(async () => {
    const contractData = require("../build/contracts/DigitalIdentityCard.json"); // Adjust the path as needed
    const networkId = await web3.eth.net.getId();
    const deployedNetwork = contractData.networks[networkId];
    digitalIdentityCardInstance = await DigitalIdentityCard.at(deployedNetwork.address);
  });

  // Test case
  it("Create a sample digital identification card", async () => {
    const name = "John Doe";
    const birthday = "2003-03-23";
    const driversLicenseNumber = 1235989;

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
