<h1> KryptoJobs2Go - Ethereum Payment Integration </h1>


## Background
Welcome to KryptoJobs2Go! This application allows customers to find fintech professionals from a list of candidates, hire them, and pay them with cryptocurrency. As the lead developer, I have integrated the Ethereum blockchain network into the application, enabling customers to make instant payments with cryptocurrency.

## How to Use
To use KryptoJobs2Go, follow these steps:

1. Launch the application by running `streamlit run krypto_jobs.py` in your terminal.
2. In the sidebar, you'll see your Ethereum account address and balance.
3. Choose a fintech professional from the drop-down menu and enter the number of hours you want to hire them for.
4. The application will calculate the total wage for the fintech professional in ether.
5. Click the "Send Transaction" button to initiate the payment process.
6. If the transaction is successful, a transaction hash will be displayed on the sidebar, and balloons will celebrate your successful payment!

## Importing Ethereum Transaction Functions
In this section, we integrated the Ethereum transaction functions into the KryptoJobs2Go application. The functions imported from `crypto_wallet.py` include:

- `generate_account`: Creates a digital wallet and Ethereum account from a mnemonic seed phrase.
- `get_balance`: Retrieves the balance of ether associated with an Ethereum account address.
- `send_transaction`: Sends an authorised transaction to the Ganache blockchain.

## Sign and Execute a Payment Transaction
To make a payment, the application calculates the candidate's wage based on the selected hourly rate and number of hours. The wage is displayed on the sidebar. When you click the "Send Transaction" button, the application initiates the payment transaction using your Ethereum account information. Once the transaction is successful, the transaction hash is displayed on the sidebar, and the payment is complete.

## Inspect the Transaction
After sending the transaction, you can inspect the details on the Ganache blockchain. Follow these steps:

1. Navigate to the Ganache accounts tab and locate your account (index 0).
2. Take a screenshot of the address, balance, and transaction (TX) count.
3. Navigate to the Ganache transactions tab and locate the transaction.
4. Click the transaction and take a screenshot of it.

## Screenshots

![Mined Blocks](https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/6.png) <br>
![Transaction Record](https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/7.png) <br>
![Validation](https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/9.png)<br>
<br>
Main Page:
<br>
(https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/5.png) <br>
<br>
Client Account Address and Ethernet Balance in Ether: <br>
(https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/1.png) <br>
(https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/2.png) <br>
(https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/3.png) <br>
(https://github.com/Isabel-SIM/WEEK-NINETEEN-HOMEWORK/blob/main/Images/4.png) <br>

Thank you for using KryptoJobs2Go!
