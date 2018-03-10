from btcpy.setup import setup
setup('mainnet')

from btcpy.structs.crypto import PrivateKey
privkey = PrivateKey.from_wif('L1XxeiQ3Y4LpeWCSEZonew7oBZoEgxWuDFK6cH9rmjfMY5FbhZfn')
pubkey = privkey.pub()
print(pubkey.to_address())
print(pubkey.to_segwit_address())

from btcpy.structs.hd import ExtendedPrivateKey, ExtendedPublicKey
xprv = ExtendedPrivateKey.decode('xprv9s21ZrQH143K2JF8RafpqtKiTbsbaxEeUaMnNHsm5o6wCW3z8ySyH4UxFVSfZ8n7ESu7fgir8imbZKLYVBxFPND1pniTZ81vKfd45EHKX73')
print(xprv.key.pub().to_address())
print(xprv.key.pub().to_segwit_address())
