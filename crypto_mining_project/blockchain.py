import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{json.dumps(self.transactions)}{self.timestamp}{self.nonce}".encode()
        return hashlib.sha256(block_data).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.transactions = []
        self.contracts = []  # List of smart contracts
        self.difficulty = difficulty

    def add_contract(self, contract):
        self.contracts.append(contract)

    def execute_contracts(self, block):
        for contract in self.contracts:
            contract.execute(block)

    def create_genesis_block(self):
        return Block(0, "0", [], time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        
    class SmartContract:
        def __init__(self, name, condition, action):
            self.name = name
            self.condition = condition  # Function that evaluates to True/False
            self.action = action        # Function to execute if condition is met

        def execute(self, block):
            if self.condition(block):
                self.action(block)

    def add_block(self):
        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            transactions=self.transactions,
            timestamp=time.time()
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.transactions = []  # Reset transaksi setelah ditambahkan ke blok

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    
    
