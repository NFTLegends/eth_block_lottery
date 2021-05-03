#!/usr/bin/env python3
#
# The script picks pseudo-random Ethereum winner account from the ACCOUNTS_FILE using as the randomness source
# the block hash on the given BLOCK_HEIGHT.
# The randomizer uses the Mersenne Twister deterministic 623-dimensionally equidistributed uniform pseudorandom
# number generator, one of the most extensively tested randomizers in existence.
#
import re
import random
from web3 import Web3


ACCOUNTS_FILE = "accounts.txt"

# PROVIDE YOUR INFURA API KEY or URL of your own node endpoint
WEB3_ENDPOINT = "https://mainnet.infura.io/v3/"

BLOCK_HEIGHT = 12362727
CONFIRMATIONS = 6


def get_winner_by_block_hash(candidates, block_hash):
    random.seed(a=block_hash)
    return random.choice(candidates)


print(f"Load accounts from {ACCOUNTS_FILE}...", end="")

with open(ACCOUNTS_FILE) as f:
    accounts = f.readlines()
    accounts = [x.strip() for x in accounts]

print("DONE")

print("Sanity checks...", end="")
for line in accounts:
    if line != line.strip():
        raise Exception(f"line {line} contains unneccessary spaces?")
    # Try to match Ethereum address regexp
    m = re.match(r"^0x[a-fA-F0-9]{40}$", line)
    if not m:
        raise Exception(f"line {line} doesn't look like eth address")

if len(accounts) != len(set(accounts)):
    raise Exception("Accounts contain duplicates?")

print("DONE")
print(f"Total accounts loaded: {len(accounts)}")

print("Connect to Web3 provider...", end="")
w3 = Web3(Web3.HTTPProvider(WEB3_ENDPOINT))
print("DONE")

current_block = w3.eth.block_number
if (current_block < BLOCK_HEIGHT + CONFIRMATIONS):
    print(f"Not enough blocks. Mined {current_block} of {BLOCK_HEIGHT + CONFIRMATIONS}")
    print(f"Need to wait {BLOCK_HEIGHT + CONFIRMATIONS - current_block} blocks")
    exit(1)

block_hash = w3.eth.get_block(BLOCK_HEIGHT).hash
print(f"Hash of block {BLOCK_HEIGHT} is {block_hash.hex()}")
print(f"See on Etherscan https://etherscan.io/block/{BLOCK_HEIGHT}")

winner = get_winner_by_block_hash(accounts, block_hash)
print(f"The winner is: {winner}")
