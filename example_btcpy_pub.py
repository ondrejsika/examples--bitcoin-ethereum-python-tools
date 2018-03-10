from btcpy.setup import setup
setup('mainnet')

from btcpy.structs.hd import ExtendedPublicKey
xpub = ExtendedPublicKey.decode('xpub6CnhBQ6cNk5m1nw5ew3rvtM8da3B9Xst2fMqUVM89z98oQHuAKSXdtTZt6qT7E3R5ZjFMxrQ1dfkfsoDjg7gL7iqrkoo3rgHMP3s49GcQfL')
print(xpub.derive('./0/0').key.to_address())
print(xpub.derive('./0/1').key.to_address())

