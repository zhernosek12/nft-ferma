"""
from web3 import Web3

RPC = 'https://polygon-rpc.com'
#RPC = 'https://mainnet.infura.io/v3/'

privatekey = '7692d2505239ca64fc2d617052a81cbc21eb3468acd5f6821b0f8920fb6415e5'

web3 = Web3(Web3.HTTPProvider(RPC))
account = web3.eth.account.privateKeyToAccount(privatekey)
address_wallet = account.address

print(address_wallet)
"""

from web3 import Web3, EthereumTesterProvider

w3 = Web3(EthereumTesterProvider())

w3.is_connected()