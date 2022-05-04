from brownie import MockV3Aggregator, accounts, config, network

FORKED_ENV = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_ENV=["development", "ganache-local"]
DECIMALS=8
STARTING_PRICE=2000_0000_0000

def get_account():
    if network.show_active() in LOCAL_ENV or network.show_active() in FORKED_ENV:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if len(MockV3Aggregator) == 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, { "from": get_account() })
    print("Mocks deployed!")