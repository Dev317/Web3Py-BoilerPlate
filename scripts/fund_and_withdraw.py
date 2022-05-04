from brownie import FundMe
from scripts.utils import get_account

def fund():
    fund_me_contract = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me_contract.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")

    fund_me_contract.fund({
        "from": account,
        "value": entrance_fee
    })

def withdraw():
    fund_me_contract = FundMe[-1]
    account = get_account()
    fund_me_contract.withdraw({
        "from": account
    })

def main():
    fund()
    withdraw()