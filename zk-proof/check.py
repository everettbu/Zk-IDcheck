import json
from web3 import Web3
from zkp import ZKProof

# Load contract ABI and address from JSON file
with open('/Users/Everett/Desktop/Zk-IDcheck/digital-id/build/contracts/DigitalIdentityCard.json') as f:
    contract_data = json.load(f)
    abi = contract_data['abi']
    address = contract_data['networks']['5777']['address']  # Replace <network_id> with the desired network ID

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Replace with your Ganache URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Retrieve accounts from Ganache
accounts = web3.eth.accounts

# Choose the first account (you can modify this logic as needed)
account_address = accounts[0]

# Instantiate contract
contract = web3.eth.contract(abi=abi, address=address)

# Retrieve identity from the contract
identity = contract.functions.getIdentity(account_address).call()

# Extract birthday from the identity
birthday = identity[1]

# Perform age verification using ZKP
zk_proof = ZKProof()  # Initialize ZKProof instance
proof_challenge = zk_proof.generate_proof(birthday)  # Generate proof
is_over_21 = zk_proof.verify_age(birthday)  # Verify age

# Print results
if is_over_21:
    print("User is over 21 years old.")
else:
    print("User is not over 21 years old.")
