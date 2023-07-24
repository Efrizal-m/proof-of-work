import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = hash

    def calculate_hash(self):
        return hashlib.sha256(
            str(self.index).encode()
            + str(self.previous_hash).encode()
            + str(self.timestamp).encode()
            + str(self.data).encode()
            + str(self.nonce).encode()
        ).hexdigest()

    def __str__(self):
        return f"Block {self.index} | Hash: {self.hash}"
