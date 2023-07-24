import hashlib

def proof_of_work(index, previous_hash, timestamp, data, difficulty):
    target = "0" * difficulty
    nonce = 0
    while True:
        block_hash = hashlib.sha256(
            str(index).encode()
            + str(previous_hash).encode()
            + str(timestamp).encode()
            + str(data).encode()
            + str(nonce).encode()
        ).hexdigest()

        if block_hash.startswith(target):
            return nonce, block_hash

        nonce += 1
