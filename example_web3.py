from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://eth.xsika.cz:8545'))

print(w3.eth.blockNumber)
print(w3.personal.newAccount('x'))

