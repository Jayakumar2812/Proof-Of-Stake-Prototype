from Crypto.Hash.SHA256 import new
from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Transaction import Transaction
from ProofOfStake import ProofOfStake
class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModal = AccountModel()
        self.pos = ProofOfStake()


    def addBlock(self,block):
        self.executeTransactions(block.transactions)
        # if self.blocks[-1].blockCount <block.blockCount:
        self.blocks.append(block)
    
    def toJson (self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data["blocks"] = jsonBlocks
        return data
    def blockCountValid(self,block):
        if (self.blocks[-1].blockCount == block.blockCount -1):
            return True
        else:
            return False
    def lastBlockHashValid(self,block):
        lastBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if (lastBlockchainBlockHash == block.lastHash):
            return True
        else:
            return False
    
    def getCoveredTransaction(self,transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print("Transaction is not covered by sender")
        return coveredTransactions

    def transactionCovered(self,transaction):

        if transaction.type == "EXCHANGE":
            return True

        senderBalance = self.accountModal.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False
    
    def executeTransactions(self,transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)

    def executeTransaction(self,transaction):
        if transaction.type == "STAKE":
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            if sender == receiver:
                amount = transaction.amount
                self.pos.update(sender,amount)
                self.accountModal.updateBalance(sender,-amount)
        sender = transaction.senderPublicKey
        receiver = transaction.receiverPublicKey
        amount = transaction.amount
        self.accountModal.updateBalance(sender,-amount)
        self.accountModal.updateBalance(receiver,amount)    
        
    def nextForger(self):
        lastBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        nextForger = self.pos.forger(lastBlockHash)
        return nextForger

    def createBlock(self,transactionFromPool,forgerWallet):
        coveredTransaction = self.getCoveredTransaction(transactionFromPool)
        self.executeTransactions(coveredTransaction)
        newBlock = forgerWallet.createBlock(coveredTransaction,BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(),len(self.blocks))
        self.blocks.append(newBlock)
        return newBlock
    
    def transactionExists(self,transaction):
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if transaction.equals(blockTransaction):
                    return True 
        return False
    
    def forgerValid(self,block):
        forgerPublicKey = self.pos.forger(block.lastHash)
        proposedBlockForger = block.forger
        if forgerPublicKey == proposedBlockForger:
            return True
        else:
            return False
    
    def transactionsValid(self,transaction):
        coveredTransaction = self.getCoveredTransaction(transaction)
        if len(coveredTransaction) == len(transaction):
            return True 
        else:
            return False