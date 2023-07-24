from blockchain import Blockchain

def main():
    blockchain = Blockchain()
    data1 = "Block 1 Data"
    data2 = "Block 2 Data"
    data3 = "Block 3 Data"

    blockchain.mine_block(data1)
    blockchain.mine_block(data2)
    blockchain.mine_block(data3)

    for block in blockchain.chain:
        print(block)

if __name__ == "__main__":
    main()
