from jsonrpc_requests import Server
bitcoind = Server('http://chains.bo:8332',
                   auth=('btcrpc', 'btc'))

address = bitcoind.getnewaddress()
privkey = bitcoind.dumpprivkey(address)

print(address)
print(privkey)

