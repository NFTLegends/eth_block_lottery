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
from progress.spinner import Spinner
import time

# constants for output coloring
LGREEN = '\033[92m'
GREEN = '\033[32m'
BOLD = '\033[1m'
ENDC = '\033[0m'


ACCOUNTS_FILE = "accounts.txt"

# PROVIDE YOUR INFURA API KEY or URL of your own node endpoint
WEB3_ENDPOINT = "https://mainnet.infura.io/v3/"

BLOCK_HEIGHT = 12362727
CONFIRMATIONS = 3


def get_winner_by_block_hash(candidates, block_hash):
    random.seed(a=block_hash)
    return random.choice(candidates)


print("")
print(f"Load accounts from {ACCOUNTS_FILE}... ", end="")

with open(ACCOUNTS_FILE) as f:
    accounts = f.readlines()
    accounts = [x.strip() for x in accounts]

print(f"{GREEN}DONE{ENDC}")

print("Sanity checks... ", end="")
for line in accounts:
    if line != line.strip():
        raise Exception(f"line {line} contains unneccessary spaces?")
    # Try to match Ethereum address regexp
    m = re.match(r"^0x[a-fA-F0-9]{40}$", line)
    if not m:
        raise Exception(f"line {line} doesn't look like eth address")

if len(accounts) != len(set(accounts)):
    raise Exception("Accounts contain duplicates?")

print(f"{GREEN}DONE{ENDC}")
print(f"Total accounts loaded: {GREEN}{len(accounts)}{ENDC}")

print("Connect to Web3 Ethereum provider... ", end="")
w3 = Web3(Web3.HTTPProvider(WEB3_ENDPOINT))
print(f"{GREEN}DONE{ENDC}")

print(f"Target block: {GREEN}{BLOCK_HEIGHT}{ENDC} ")
print(f"Confirmations: {GREEN}{CONFIRMATIONS}{ENDC} ")
print("")

block_hash = None
spinner = Spinner()
while True:
    current_block = w3.eth.block_number
    got_confirmations = current_block - BLOCK_HEIGHT
    if current_block < BLOCK_HEIGHT:
        spinner.message = f"Waiting for target block. {current_block} of {BLOCK_HEIGHT} "
        spinner.update()
        for i in range(10):
            time.sleep(0.1)
            spinner.next()
        continue
    if block_hash is None:
        spinner.clearln()
        print(f'Target block {current_block} mined!')
        block_hash = w3.eth.get_block(BLOCK_HEIGHT).hash
        print(f"Hash of the block {BLOCK_HEIGHT} is {GREEN}{block_hash.hex()}{ENDC}")
        print(f"See it on Etherscan https://etherscan.io/block/{BLOCK_HEIGHT}")
    if got_confirmations <= CONFIRMATIONS:
        spinner.message = f'Waiting confirmations {got_confirmations} of {CONFIRMATIONS} '
        spinner.update()
        spinner.next()
        for i in range(10):
            time.sleep(0.1)
            spinner.next()
        continue
    spinner.clearln()
    print(f'Target block {current_block} confirmed!')
    break

winner = get_winner_by_block_hash(accounts, block_hash)
print("")
print(f"The winner is: {BOLD}{GREEN}{winner}{ENDC}")
print("")
