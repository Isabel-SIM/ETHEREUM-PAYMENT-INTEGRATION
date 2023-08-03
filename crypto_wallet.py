# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons.
# By using import statements, you will integrate this `crypto_wallet.py` Python script
# into the KryptoJobs2Go interface program that is found in the `krypto_jobs.py` file.

################################################################################
# Imports
import os
import requests
from dotenv import load_dotenv

load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
# from web3 import utils

from web3 import Web3
from eth_account import Account


################################################################################
# Wallet functionality


def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.from_key(private)

    return account


def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)


    # Convert Wei value to ether
    ether = wei_balance / 10 ** 18  # 1 Ether = 10^18 Wei

    # Return the value in ether
    return ether


def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    """Sign and send an Ethereum transaction"""
    # Convert amount from ether to Wei
    amount_wei = w3.toWei(wage, 'ether')

    gasEstimate = w3.eth.estimateGas(
        {"to": to, "from": account.address, "value": amount_wei}
    )


    # Prepare the transaction details
    transaction = {
        "to": to,
        "from": account.address,
        "value": amount_wei,
        "gas": gasEstimate,
        'gasPrice': 20000000000,
        'nonce': w3.eth.getTransactionCount(account.address),
    }

    # Sign the transaction
    signed_transaction = account.signTransaction(transaction)

    # Send the transaction
    transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    return transaction_hash.hex()

   