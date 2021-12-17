from BlockchainUtils import BlockchainUtils

class Lot():

    def __init__(self,publicKey,iteration,lastBlockHash) :
        self.publicKey = publicKey
        self.iteration = iteration
        self.lastBlockHash = lastBlockHash

    def lotHash(self):
        hashData = self.publicKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = BlockchainUtils.hash(hashData).hexdigest()
        return hashData



