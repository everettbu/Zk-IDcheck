pragma solidity >=0.4.22 <0.9.0;

contract DigitalIdentityCard {
    struct Identity {
        string name;
        uint256 birthday;
        uint256 driversLicenseNumber;
        address owner;
    }

    mapping(address => Identity) public identities;

    event IdentityCreated(address indexed owner, string name, uint256 birthday, uint256 driversLicenseNumber);

    function createIdentity(string memory _name, uint256 _birthday, uint256 _driversLicenseNumber) public {
        require(identities[msg.sender].driversLicenseNumber == 0, "Identity already exists");
        identities[msg.sender] = Identity(_name, _birthday, _driversLicenseNumber, msg.sender);
        emit IdentityCreated(msg.sender, _name, _birthday, _driversLicenseNumber);
    }

    function getIdentity(address _owner) public view returns (string memory, uint256, uint256) {
        Identity memory identity = identities[_owner];
        return (identity.name, identity.birthday, identity.driversLicenseNumber);
    }
}
