const DigitalIdentityCard = artifacts.require("DigitalIdentityCard");

module.exports = function(deployer) {
  deployer.deploy(DigitalIdentityCard);
};
