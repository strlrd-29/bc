import os
import pprint
import requests

from dotenv import load_dotenv
from eth_account import Account
from web3 import Web3

load_dotenv()

private_key = os.getenv('PRIVATE_KEY')
rpc_endpoint = os.getenv('RPC_ENDPOINT')
contract_address = os.getenv('CONTRACT_ADDRESS')

request_id = 0

# create persistent HTTP connection
session = requests.Session()
pp = pprint.PrettyPrinter()

account = Account.from_key(private_key)

# Defining some functions


def createJSONRPCRequestObject(_method: str, _params: list[str], _requestId: int):
    return {"jsonrpc": "2.0",
            "method": _method,
            "params": _params,
            "id": _requestId}, _requestId+1


def postJSONRPCRequestObject(_HTTPEnpoint: str, _jsonRPCRequestObject: dict):
    response = session.post(_HTTPEnpoint,
                            json=_jsonRPCRequestObject,
                            headers={'Content-type': 'application/json'})

    return response.json()


# Get Transaction count (nonce)
request_object, request_id = createJSONRPCRequestObject(
    'eth_getTransactionCount', [contract_address, 'latest'], request_id)
response_object = postJSONRPCRequestObject(rpc_endpoint, request_object)

nonce = int(response_object['result'], base=16)

request_object, request_id = createJSONRPCRequestObject(
    "eth_gasPrice", [], request_id)
response_object = postJSONRPCRequestObject(rpc_endpoint, request_object)


gas_price = int(response_object['result'], base=16)

request_object, request_id = createJSONRPCRequestObject(
    "eth_chainId", [], request_id)
response_object = postJSONRPCRequestObject(rpc_endpoint, request_object)

chain_id = int(response_object['result'], base=16)

print(f'Nonce of {contract_address} is {nonce}')
print(f'Gas Price of {contract_address} is {gas_price}')
print(f'Chain id of {contract_address} is {chain_id}')

new_greeting = 'Hello Universe!'
function = 'setGreeting(string)'
param = bytes(new_greeting, 'utf-8').hex()

methodId = Web3.keccak(text=function)[0:4].hex()

data = methodId + param

transaction_dict = {
    'from': account.address,
    'to': contract_address,
    'gasPrice': gas_price,
    'gas': 2000000,
    'nonce': nonce,
    'data': data,
    'chainId': chain_id
}

signed_transaction_dict = Account.sign_transaction(
    transaction_dict, private_key)
params = [signed_transaction_dict.rawTransaction.hex()]

print('executing {} with value {}'.format(function, param))
requestObject, requestId = createJSONRPCRequestObject(
    'eth_sendRawTransaction', params, request_id)
responseObject = postJSONRPCRequestObject(rpc_endpoint, requestObject)
print(responseObject)

transactionHash = responseObject['result']
print('transaction hash {}'.format(transactionHash))
