from jsonrpc_requests import Server
eth = Server('http://eth.xsika.cz:8545')

print(eth.eth_blockNumber())
print(eth.personal_newAccount(''))

