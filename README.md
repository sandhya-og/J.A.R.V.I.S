# Jarvis

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction
An effort to create intelligent personal assistant for your computers and laptops which can also be called as one stop shop for essential functionalities of system functioning. This can be used to complete your tasks with your voice command and chat command, designed to improve the productivity. 

## Features
J.A.R.V.I.S offers a wide range of functionalities to enhance user experience and productivity:

1. **Play YouTube on User’s Demand**
2. **Search and Provide Details for Any Required Information**
3. **Send Emails: Compose and send emails with optional attachments using smtplib.**
4. **Daily News Updates using Bs4 library**
5. **Basic System Functionalities: files, apps, sleep, restart, shutdown, System Information**
6. **Weather using py_weather library**
7. **Chat with User**
8. **Access Social Media with password manager using cryptography.fernet**
9. **Language Flexibility**

## Installation
### Prerequisites
- Python 3.12 or higher
- Pip package manager

### Steps
1. Clone the repository:
   ```sh
   git clone [https://github.com/yourusername/jarvis.git](https://github.com/sandhya-og/J.A.R.V.I.S.git)
   cd jarvis
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
   
5. Run the application:
   ```sh
   python main.py
   ```

## Usage
Once the installation is complete, you can start using Jarvis. Use the command line or voice commands to interact with Jarvis. Refer to commands.py in root directory for keywords that trigger the specific actions:

Enjoy using J.A.R.V.I.S and enhance your productivity with this intelligent personal assistant!



Practical 1
Q. A simple client class that generates the public key and the private key by using the built in python RSA algorithm and test it
Q. A simple client class that generates the public key and the private key ledgers by using the built in python RSA algorithm and test it
Public Key: Shared with everyone; used to encrypt data.
Private Key: Kept secret; used to decrypt data.
PKCS1: Stands for Public Key Cryptography Standard #1. It defines the mathematical format for RSA keys and how encryption/signatures should be structured.
OAEP (Optimal Asymmetric Encryption Padding): A padding scheme used with PKCS1 that adds randomness to the encryption process. This ensures that if you encrypt the same message twice, the output (ciphertext) will look different each time, preventing hackers from recognizing patterns.
Feature
Code A (Encryption Flow)
Code B (Identity/Blockchain Flow)
Primary Goal
To securely hide a message so only the receiver can read it.
To create a unique ID for a user (often used in Blockchain).
Output
A scrambled, unreadable message (Ciphertext).
A long hexadecimal string representing the user's "Identity".
Key Size
Uses a stronger 2048-bit key.
Uses a smaller 1024-bit key.
Functionality
Focuses on encrypt() and decrypt() methods.
Focuses on exportKey() and hexlify() to show the key as text.


Create a Python script to generate an RSA public/private key pair using the PyCryptodome library, and demonstrate the encryption and decryption of a text message using the PKCS1_OAEP padding standard.
Pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


#generate RSA Key Pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()


#create cipher objects
encryptor = PKCS1_OAEP.new(public_key)
decryptor = PKCS1_OAEP.new(private_key)


#message to encypt
message = b"Hello RSA!"


#encrypt message
encrypted = encryptor.encrypt(message)
print("Encrypted: ", encrypted)


#decrypt message
decrypted = decryptor.decrypt(encrypted)
print("Decrypted: ", decrypted.decode())





Design a client class that generates an RSA key pair and provides a property to export the Public Key as a hexadecimal string (DER format) to serve as a unique client identity.
import binascii
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self.private_key = RSA.generate(1024, random)
        self.public_key = self.private_key.publickey()
        self.signer = PKCS1_v1_5.new(self.private_key)


    @property
    def identity(self):
        return binascii.hexlify(self.public_key.exportKey(format='DER')).decode('ascii')
    
TYIT = Client()
print("Public key: ",TYIT.identity)




Practical 2 - No of Bitcoins
Find the number of Bitcoins by applying the equation over a defined value. 
Formula: Number of BTC = Amount in INR / Price of 1 BTC in INR
investment = float(input("Enter your investment: "))
btc_price = float(input("Enter current price of 1 BTC: "))
btc_amt = investment/btc_price
print(f"You can buy {btc_amt:.2f} BTC")






Practical 3: Ethereum transaction
Part 1: Create a transaction class to send and receive money and test it. 
Operations:
1. Create an account 
2. Deposit: Account = Self balance + amount 
3. Withdraw: Self balance = self-balance – amount 
4. Enquiry
class Bank:
    def __init__(self):
        self.balance= 0
        print("Accound created!")


    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited: ", amount)


    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew: ", amount)
        else:
            print("\n Insufficient Balance")
            
    def enquiry(self):
        print("\n Balance in the account is: ", self.balance)


account = Bank()
account.deposit()
account.withdraw()
account.enquiry()





Part 2: Setting Up Eth Dev Environment
Download etherum
Download ganache
Instal metamask extension
1. Ganache as the Local "Ethereum"
Instead of deploying code to the real Ethereum network (which costs real money/Gas), you run Ganache. It acts as a personal, local instance of Ethereum.
It provides you with 10 fake accounts, each pre-funded with 100 test Ether.
Transactions happen instantly without waiting for global miners.
2. MetaMask as the Connector
MetaMask is a browser extension that allows you to interact with blockchains. By default, it points to the real Ethereum Mainnet, but you can change its settings to point to your local Ganache network.
The Bridge: You configure MetaMask with the RPC URL (usually http://127.0.0.1:7545) and Chain ID provided by Ganache.
Importing Funds: You can copy a "Private Key" from one of the Ganache accounts and paste it into MetaMask. This gives your browser-based wallet access to that fake Ether for testing.

Part 3: Ethereum Basics Ethereum Wallet, Ether transactions
Click on open wallet in metamask
Click on 3 lines > select network > add custom network 
In default RPC URL > click on add RPC URL
Go to ganache > copy the RPC server > paste it in RPC URL in metamask and click on Add url
Give network name: Localhost 8545
Chain ID: 1337
Currency symbol: ETH
Click on save
Go to accounts > add wallet > import an account 
Go to Ganache > Click on key > copy private key
In Metamask paste the private key in import an account tab > click on save 
Click on etherum > click on send 
Go to ganache > copy 2nd account public key address 
Paste it on TO input field in send section > add amount : 20 > click continue > click confirm
   


Practical 4: Smart Contracts Solidity basics, Writing and Deploying Smart Contract
Solidity works on EVM [Ethereum Virtual Machine] to run Smart Contract. Difference between Solidity & Other Programming 
SOLIDITY
OTHER PROGRAMMING LANGUAGES
SMART CONTRACTS
GENERAL PURPOSE
EVM
OS, SERVER
IMMUTABLE
MODIFIED
GAS FEE
FREE
BLOCKCHAIN
FILES, DATABASE, CLOUD
DECENTRALIZED
CENTRALIZED


PART 1:
Go to remix ide > click on create new workspace > select blank > give name as TYIT > click on finish
In file explorer Click on create > new file > tytokens
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.31;

contract TOKENS_SC{
    string public name = "tyTokens";
    string public symbol = "TYIT";
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    constructor(uint256 initialSupply){
        totalSupply = initialSupply;
        balanceOf[msg.sender] = initialSupply;
    }
}

Go to solidity compiler tab > compile tytokens.sol 
Go to deploy and run transactions tab > enter initialSupply - 1000000 in textbox beside deploy button > click on deploy
Go to deployed contracts > copy paste the account in balanceOf and click on balanceOf > click on name, symbol and totalSupply
 
PART 2:
Edit the code to add the ability to actually move tokens between users
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.31;

contract TOKENS_SC{
    string public name = "tyTokens";
    string public symbol = "TYIT";
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    constructor(uint256 initialSupply){
        totalSupply = initialSupply;
        balanceOf[msg.sender] = initialSupply;
    }

    function transfer(address toWhom, uint256 value) public returns(bool success){
        require(balanceOf[msg.sender] >= value, "Insufficient token");
        balanceOf[msg.sender] -= value;
        balanceOf[toWhom] += value;
        return true;
    }
}

Go to solidity compiler tab > compile tytokens.sol 
Go to deploy and run transactions tab > enter initialSupply - 1000000 in textbox beside deploy button > click on deploy
Using same account from where you deployed > paste same account in balanceOf
Now select another account, copy and paste in transfer > expand transfer > enter value:800000 > and again select account from which you deployed > click on transact
Click on balanceOf, name, symbol, totalSupply

 

Practical 5: Create a basic Defi (Decentralised Financial system)
PART 1:
Go to remix ide > click on create new workspace > select blank > give name as TYIT > click on finish
In file explorer Click on create > new file > ERC
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract MyToken is ERC20{ 
    constructor() ERC20("MyToken", "MTL"){ 
        _mint(msg.sender, 1_000_000 ether); 
    }
}

Go to solidity compiler tab > compile ERC 
Go to deploy and run transactions tab > click on deploy
Go to deployed contracts > copy paste the account in balanceOf and click on balanceOf > click on name, symbol and totalSupply
Now select another account, copy and paste in transfer > expand transfer > enter value:800000 > and again select account from which you deployed > click on transact

PART 2:
In file explorer Click on create > new file > Stake
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
contract SimpleStaking{
    IERC20 public token;
    mapping(address=>uint256) public stakes;

    constructor(address _token){
        token = IERC20(_token);
    }

    function stake(uint256 amount) external{
        require(amount>0,"Zero amount");
        token.transferFrom(msg.sender,address(this),amount);
        stakes[msg.sender]+=amount;
    }
    
    function unstake(uint256 amount) external {
        require(stakes[msg.sender]>=amount,"Not enough stake");
        stakes[msg.sender]-=amount;
        token.transfer(msg.sender, amount);
    }

}

Go to solidity compiler tab > compile Stake 
Go to deploy and run transactions tab of Stake.sol> enter the erc token id > paste it on textbox beside deploy button > click on deploy
Go to deployed contracts of erc > enter stake token id > enter amount – 6000000 > click on transact
Go to deployed contracts of stake > enter value in stake and click on it: 6000000 > enter value in stake and click on it: 3000000
In stakes placeholder > copy account of stake.sol > paste and click on stakes
Click on token

 
Practical 6: 
PART 1: Interaction with smart contract and web3
Q. Write a smart contract using truffle and Node.js
Click on open wallet in metamask
Click on 3 lines > select network > add custom network 
In default RPC URL > click on add RPC URL
Go to ganache > copy the RPC server > paste it in RPC URL in metamask and click on Add url
Give network name: Localhost 8545
Chain ID: 1337
Currency symbol: ETH
Click on save
Go to accounts > add wallet > import an account 
Go to Ganache > Click on key > copy private key
In Metamask paste the private key in import an account tab > click on save 
Download node 16-18 any version bcoz truffle works only with those versions
Make a folder named blockchain on desktop 
Open folder in vs code and run this cmd:
npm install -g truffle
npm install truffle lite-server
npx truffle init
uncommit development line from -67-71, change port to default 7545, and on line 109, change version from 0.8.20 to 0.8.0
create new file named: 1_deploy.js in migrations folder
const Add = artifacts.require("Add");

module.exports = function(deployer){
    deployer.deploy(Add);
}


create new file named: add.sol.js in contracts folder
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Add {
    function add(uint a, uint b) public pure returns (uint) {
        return a + b;
    }
}


run CMD: 
npx truffle compile –all
npx truffle migrate --reset


PART 2: Introduction to DApp
Q. Write a program to create Dapp
Create index.html:
<!DOCTYPE html>
<html>
<head>
    <title>Add DApp</title>
    <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
</head>
<body>
    <h2>Practical 10: Simple Add DApp</h2>
    <button onclick="connectWallet()">Connect Wallet</button>
    <p id="walletAddress"></p>
    <hr>
    <input type="number" id="num1" placeholder="Enter first number">
    <input type="number" id="num2" placeholder="Enter second number">
    <button onclick="calculateSum()">Calculate Sum</button>
    <h3 id="resultText">Result: </h3>

    <script>
        let web3;
        let contract;
        // COPY THIS FROM: build/contracts/Add.json (the "abi" array)
        const abi = [ { "inputs": [ { "internalType": "uint256", "name": "a", "type": "uint256" }, { "internalType": "uint256", "name": "b", "type": "uint256" } ], "name": "add", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "pure", "type": "function" } ];
        // COPY THIS FROM YOUR TERMINAL OUTPUT
        const contractAddress = "0x120D68bc7Da47806fD123360Ed1eFA0F18c08111"; 

        async function connectWallet() {
            if (window.ethereum) {
                web3 = new Web3(window.ethereum);
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const accounts = await web3.eth.getAccounts();
                document.getElementById('walletAddress').innerText = "Connected: " + accounts[0];
                contract = new web3.eth.Contract(abi, contractAddress);
            } else {
                alert("Please install MetaMask!");
            }
        }

        async function calculateSum() {
            const val1 = document.getElementById('num1').value;
            const val2 = document.getElementById('num2').value;
            // Calling the 'add' function from your add.sol [cite: 296]
            const result = await contract.methods.add(val1, val2).call();
            document.getElementById('resultText').innerText = "Result: " + result;
        }
    </script>
</body>
</html>





Right click > Open with live server extension
 

Practical 7: Finding percentage change in price
from math import log
final = int(input("Enter final price: "))
initial = int(input("Enter initial price: "))
percent_change = ((final - initial) / initial) * 100
log_return = log(final / initial)
print(f"Percent change: {percent_change:.2f}%")
print(f"Log return: {log_return:.2f}")





Practical 8: Use of Ethereum
Q1. Write a solidity program of creating a smart contract for attendance
Go to remix ide > click on create new workspace > select blank > give name as TYIT > click on finish
In file explorer Click on create > new file > Attendence
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Attendance {
    //Store roll number 
    mapping(uint256 => bool) public isPresent;
    //Constructor initializes rll number
    constructor(uint256[] memory rollno) {
        for (uint256 i=0; i< rollno.length; i++) {
            isPresent[rollno[i]] = true;
        }
    }
    //Check attendance
    function attend(uint256 roll) public view returns(bool){
        return isPresent[roll];
    }
}

Go to solidity compiler tab > compile ERC 
Go to deploy and run transactions tab > add [1, 2, 3] in input placeholder for deploy > click on deploy


Q2. Write a solidity program of creating a smart contract for attendance
Go to remix ide > click on create new workspace > select blank > give name as TYIT > click on finish
In file explorer Click on create > new file > Attendence
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;
contract Donation {
    // Store total donation amount
    uint256 public totalDonations;
    // Store donation amount by donor address
    mapping(address => uint256) public donations;
    
    constructor() {
        totalDonations = 0;
    }
    // Function to donate Ether
    function donate() public payable {
        require(msg.value > 0, "Donation must be greater than 0");
        donations[msg.sender] += msg.value;
        totalDonations += msg.value;
    }
    // Check donation amount of a specific donor
    function checkDonation(address donor) public view returns (uint256) {
        return donations[donor];
    }
}

Go to solidity compiler tab > compile ERC 
Go to deploy and run transactions tab > click on deploy
Add wei as 10 > expand donation contract > click on donate > copy paste same account address into donations field > click on donations
Click on totalDonations




