from block import Block
from proof_of_work import proof_of_work
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block", 0, "0")

    def add_block(self, block):
        self.chain.append(block)

    def mine_block(self, data):
        previous_block = self.chain[-1]
        index = len(self.chain)
        timestamp = int(time.time())
        nonce, hash = proof_of_work(index, previous_block.hash, timestamp, data, self.difficulty)
        new_block = Block(index, previous_block.hash, timestamp, data, nonce, hash)
        self.add_block(new_block)
        return new_block
