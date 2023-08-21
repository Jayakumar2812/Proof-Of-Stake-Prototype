# Installation 
* Install python
* ``` pip install -r requirements.txt ``` or ```pip3 install -r requirements.txt ``` depending upon the version of python.
  
# Commands and interactions
* To run this code, open a new command terminal and navigate to this directory. enter: python main.py 0.0.0.0 10001 5000
* to add a new node, do the same as above but with different port, api-port
* to run a transaction "python interaction.py"
* to view blockchain "host://api-port/blockchain"
* to add RSA keypairs to a node, you can include it when running the program(step 1) by including the relative path of the file



# Proof-Of-Stake-Prototype
* Nodes automatically sync with each other when a transaction is added to blockchain
* API's are added for blockchain data,Transaction Pools,Transaction(/blockchain,/transactionPool,/transaction)
* P2P is established, Therefore nodes can communicate between each other in secured way
* Real life Validations checks are implemented for checking blocks validity
* Block forger are determined proof of stake mechanism (percentage of stake is directly proportional to the chances of being the next forger)
* Keys folder contains the demo private/public Keys for testing.

 
