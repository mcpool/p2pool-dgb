from p2pool.bitcoin import networks

PARENT = networks.nets['digibyte']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 50 # shares diff regulation
SPREAD = 10 # blocks
IDENTIFIER = '48a4ebc31b798115'.decode('hex')
PREFIX = '5685a276c2dd81db'.decode('hex')
P2P_PORT = 8022
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9022
BOOTSTRAP_ADDRS = 'dgb.mastercryptopool.net dgb2.mastercryptopool.net dgb3.mastercryptopool.net p2pool.e-pool.net:29992'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
