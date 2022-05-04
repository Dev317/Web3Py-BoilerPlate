from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utils import get_account, deploy_mocks, LOCAL_ENV
from web3 import Web3

def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_ENV:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me_contract = FundMe.deploy(
    price_feed_address
    ,{
        "from": account,
        "gas": 2000000,
        "gasPrice": Web3.toWei('50', 'gwei')
    }, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me_contract.address}")
    return fund_me_contract

def main():
    deploy_fund_me()