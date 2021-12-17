from Transaction import Transaction
from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests

def postTransaction(sender,receiver,amount,type):
    transaction = sender.createTransaction(receiver.publicKeyString(),amount,type)

    url = "http://localhost:5000/transaction"
    package = {"transaction":BlockchainUtils.encode(transaction)}
    request = requests.post(url,json=package)
    print(request.text)

if __name__ == "__main__":
    jk = Wallet()
    aravind = Wallet()
    aravind.fromKey("keys/stakerPrivateKey.pem")
    exchange = Wallet()
    
    #forger : genesis
    
    postTransaction(exchange,aravind,100,"EXCHANGE")
    postTransaction(exchange,jk,100,"EXCHANGE")
    postTransaction(exchange,jk,100,"EXCHANGE")

    postTransaction(aravind,aravind,25,"STAKE")
    postTransaction(aravind,jk,1,"TRANSFER")
    postTransaction(aravind,jk,1,"TRANSFER")
    

