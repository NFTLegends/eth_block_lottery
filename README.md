# NFTLegends BlockHash-based lottery

## About

The script picks pseudo-random Ethereum winner account from the list using native blockchain randomness source - the blockhash on the given block height.

It uses the “Mersenne Twister” deterministic 623-dimensionally equidistributed uniform pseudorandom number generator, one of the most extensively tested randomizers in existence.

## Provenance

* Block: **[12362727](https://etherscan.io/block/countdown/12362727)** on Ethereum Mainnet #1
* Estimated Target Date: **Mon May 03 2021 17:58:29 GMT**

Accounts collected through the form were checked to comply ethereum account format (42-digit hex string starting with '0x').
Duplicates were removed and items sorted alphabetically. See [refine_eth_accounts.py](refine_eth_accounts.py) script for details.

* Refined accounts list: **[accounts.txt](accounts.txt)**
* Participants total: **13208**



## How to verify

Just run the [lottery.py](lottery.py) after the target block got mined + 6 confirmations passed.

```sh
pip install -r requirements.txt
python3 lottery.py
```

The output:

```sh
Load accounts from accounts.txt...DONE
Sanity checks...DONE
Total accounts loaded: 13208
Connect to Web3 provider...DONE
Hash of block 12361500 is 0x6d9987ca8fbca75658086c8678c04eccb6cfff3666afd7e11d9d2bf81004ada3
See on Etherscan https://etherscan.io/block/12361500
The winner is: <Winner's Account>
```
