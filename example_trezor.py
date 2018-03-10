from trezorlib.client import TrezorClient
from trezorlib.transport import get_transport


client = TrezorClient(get_transport())

bip32_path = client.expand_path("44'/0'/0'/0/0")
print(client.get_address('Bitcoin', bip32_path))

bip32_path = client.expand_path("44'/0'/0'/0/1")
print(client.get_address('Bitcoin', bip32_path))

