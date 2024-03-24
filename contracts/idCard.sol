pragma solidity >=0.4.22 <0.9.0;

contract DigitalIdentityCard {
    struct Identity {
        string name;
        string birthday;
        uint256 driversLicenseNumber;
        address owner;
    }

    mapping(address => Identity) public identities;
    mapping(uint256 => bool) public isDriverLicenseNumberRegistered; // Mapping to track registered driver's license numbers

    event IdentityCreated(address indexed owner, string name, string birthday, uint256 driversLicenseNumber);

    function createIdentity(string memory _name, string memory _birthday, uint256 _driversLicenseNumber) public {
        // Check if driver's license number is already registered
        require(!isDriverLicenseNumberRegistered[_driversLicenseNumber], "Driver's license number already registered");

        identities[msg.sender] = Identity(_name, _birthday, _driversLicenseNumber, msg.sender);
        emit IdentityCreated(msg.sender, _name, _birthday, _driversLicenseNumber);

        // Mark the driver's license number as registered
        isDriverLicenseNumberRegistered[_driversLicenseNumber] = true;
    }

    function getIdentity(address _owner) public view returns (string memory, string memory, uint256) {
        Identity memory identity = identities[_owner];
        return (identity.name, identity.birthday, identity.driversLicenseNumber);
    }
}
