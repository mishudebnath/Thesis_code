from solcx import compile_standard, install_solc, get_installed_solc_versions
from web3 import Web3
import json

# Install Solidity compiler version if not already installed
solc_version = '0.8.0'
if solc_version not in get_installed_solc_versions():
    install_solc(solc_version)

# Solidity source code
contract_source_code = '''
pragma solidity ^0.8.0;

contract PredictionStore {
    struct Result {
        string student_id;
        string prediction;
    }

    mapping(string => Result) public results;

    function storeResult(string memory student_id, string memory prediction) public {
        results[student_id] = Result(student_id, prediction);
    }
}
'''

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "PredictionStore.sol": {
            "content": contract_source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        }
    }
}, solc_version=solc_version)

# Get bytecode and abi
bytecode = compiled_sol['contracts']['PredictionStore.sol']['PredictionStore']['evm']['bytecode']['object']
abi = json.loads(compiled_sol['contracts']['PredictionStore.sol']['PredictionStore']['metadata'])['output']['abi']

# Connect to the local Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if connected
if web3.is_connected():
    print("Successfully connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Set up account details
account = '0xa9e487989937d6CD1c140aC4ea3A8be9fb7eB680'
private_key = '0xb077533417c6732fc13c15b229da0ed6337e80b297d646f3e28823c902ba7d29'

# Set up the contract in Python
PredictionStore = web3.eth.contract(abi=abi, bytecode=bytecode)

# Build the transaction
transaction = PredictionStore.constructor().build_transaction({
    'from': account,
    'nonce': web3.eth.get_transaction_count(account),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei')
})

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the transaction
txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

# Wait for the transaction to be mined
txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

# Print the contract address
contract_address = txn_receipt.contractAddress
print("Contract deployed at address:", contract_address)
