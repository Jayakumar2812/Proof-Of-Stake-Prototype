

class TransactionPool():

    def __init__(self):
        self.transactions = []

    def addTransaction(self,tranasaction):
        self.transactions.append(tranasaction)
    
    def transactionExists(self,transaction):
        for poolTransacion in self.transactions:
            if (poolTransacion.equals(transaction)) :
                return True 
        return False

    def removeFromPool(self,transactions):
        newPoolTransaction = []
        for PoolTransaction in self.transactions:
            insert = True
            for transaction in transactions:
                if PoolTransaction.equals(transaction):
                    insert = False
            if insert == True :
                newPoolTransaction.append(PoolTransaction)
        self.transactions = newPoolTransaction

    def forgerRequired(self):
        if (len(self.transactions)>=3):
            return True
        else:
            return False














        



