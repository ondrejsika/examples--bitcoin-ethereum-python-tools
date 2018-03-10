from web3 import Web3, HTTPProvider
from solc import compile_source

with open('greeter.sol', 'r') as f:
    contract_source_code = f.read()

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Greeter']

w3 = Web3(HTTPProvider('http://eth.xsika.cz:8545'))
con = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
# con.deploy()

