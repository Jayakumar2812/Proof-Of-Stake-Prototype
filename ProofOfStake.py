

from BlockchainUtils import BlockchainUtils
from Lot import Lot


class ProofOfStake():

    def __init__(self):
        self.stakers = {}
        self.setGenesisNodeStake()
    
    def setGenesisNodeStake(self):
        genesisPublicKey = open("keys/genesisPublicKey.pem").read()
        self.stakers[genesisPublicKey] = 1

    def update(self,publicKeyString,stake):
        if publicKeyString in self.stakers.keys():
            self.stakers[publicKeyString] += stake
        
        else:
            self.stakers[publicKeyString] = stake
    
    def get(self,publicKeyString):
        if publicKeyString in self.stakers.keys():
            return self.stakers[publicKeyString]
        else:
            return None
    
    def validatorLots(self,seed):
        lots = []
        for validator in self.stakers.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator,stake+1,seed))
        return lots
    
    def winnerLot(self,lots,seed):
        winnerLot = None
        leastOffset = None
        ReferenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(),16)
        for lot in lots:
            lotIntValue = int(lot.lotHash(),16)
            offset =abs(lotIntValue - ReferenceHashIntValue)
            if leastOffset is None or offset < leastOffset:
                leastOffset = offset
                winnerLot = lot
        return winnerLot

    def forger(self,lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot =self.winnerLot(lots,lastBlockHash)
        return winnerLot.publicKey
 