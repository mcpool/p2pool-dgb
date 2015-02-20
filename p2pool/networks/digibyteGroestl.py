from p2pool.bitcoin import networks

PARENT=networks.nets['digibyteGroestl'],
SHARE_PERIOD=15, # seconds target spacing
CHAIN_LENGTH=24*60*60//10, # shares
REAL_CHAIN_LENGTH=24*60*60//10, # shares
TARGET_LOOKBEHIND=50, # shares diff regulation
SPREAD=30, # blocks
IDENTIFIER='48a4ebc31b798114'.decode('hex'),
PREFIX='5685a276c2dd71db'.decode('hex'),
P2P_PORT=5020,
MIN_TARGET=0,
MAX_TARGET=2**256//2**20 - 1,
PERSIST=True,
WORKER_PORT=5021,
BOOTSTRAP_ADDRS='dgbsha.mastercryptopool.net dgbsha2.mastercryptopool.net dgbsha3.mastercryptopool.net'.split(' '),
ANNOUNCE_CHANNEL='#p2pool-alt',
VERSION_CHECK=lambda v: True,
