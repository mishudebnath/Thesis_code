from web3 import Web3
import json

# Connect to the local Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if connected
if web3.is_connected():
    print("Successfully connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Deployed contract address and ABI
contract_address = '0x70153cE917104c833173Caf5a98d28a41736AB03'
abi = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "student_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "prediction",
                "type": "string"
            }
        ],
        "name": "storeResult",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "results",
        "outputs": [
            {
                "internalType": "string",
                "name": "student_id",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "prediction",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Set up the contract in Python
prediction_store = web3.eth.contract(address=contract_address, abi=abi)

# Set up account details
account = '0xa9e487989937d6CD1c140aC4ea3A8be9fb7eB680'
private_key = '0xb077533417c6732fc13c15b229da0ed6337e80b297d646f3e28823c902ba7d29'

# Function to store a result
def store_result(student_id, prediction):
    transaction = prediction_store.functions.storeResult(student_id, prediction).build_transaction({
        'from': account,
        'nonce': web3.eth.get_transaction_count(account),
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

# Function to get a result
def get_result(student_id):
    result = prediction_store.functions.results(student_id).call()
    return result

# Store a new result
student_id = '12345'
prediction = 'Passed'
receipt = store_result(student_id, prediction)
print("Transaction receipt:", receipt)

# Get the stored result
stored_result = get_result(student_id)
print("Stored result:", stored_result)
