from p2pool.bitcoin import networks

PARENT = networks.nets['digibyteSha']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 50 # shares diff regulation
SPREAD = 10 # blocks
IDENTIFIER = '48a4ebc31b798115'.decode('hex')
PREFIX = '5685a276c2dd81db'.decode('hex')
P2P_PORT = 5010
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 5011
BOOTSTRAP_ADDRS = 'dgbsha.mastercryptopool.net dgbsha2.mastercryptopool.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
