# NFTLegends BlockHash-based lottery

## About

The script picks pseudo-random Ethereum winner account from the list using native blockchain randomness source - the blockhash on the given block height.

It uses the “Mersenne Twister” deterministic 623-dimensionally equidistributed uniform pseudorandom number generator, one of the most extensively tested
randomizers in existence.

## Provenance

* Block: **[12362727](https://etherscan.io/block/countdown/12362727)** on Ethereum Mainnet #1
* Estimated Target Date: **Mon May 03 2021 17:58:29 GMT**
* Candidate accounts: **accountlist.json** (duplicates are removed, items sorted alphabetically)

## Howto

* Just run the lottery.py after the target block got mined
