from flask import Flask, jsonify, request, render_template, redirect, url_for

from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify({'chain': chain_data, 'length': len(chain_data)}), 200

@app.route('/transactions/new', methods=['GET', 'POST'])
def new_transaction():
    if request.method == 'GET':
        return render_template('transaction.html')
    elif request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        amount = request.form['amount']

        if not sender or not recipient or not amount:
            return 'Invalid transaction data', 400

        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        blockchain.add_transaction(transaction)
        return redirect(url_for('home'))

@app.route('/mine', methods=['GET'])
def mine_block():
    blockchain.add_block()
    latest_block = blockchain.get_latest_block()
    response = {
        'message': 'Block mined successfully!',
        'block': {
            'index': latest_block.index,
            'transactions': latest_block.transactions,
            'hash': latest_block.hash,
            'previous_hash': latest_block.previous_hash,
            'nonce': latest_block.nonce
        }
    }
    return jsonify(response), 200

@app.route('/visualize', methods=['GET'])
def visualize():
    return render_template('index.html')

@app.route('/contracts/new', methods=['POST'])
def add_contract():
    data = request.get_json()
    required_fields = ['name', 'condition', 'action']

    if not all(field in data for field in required_fields):
        return 'Invalid contract data', 400

    condition = eval(data['condition'])  # Example: lambda block: len(block.transactions) > 5
    action = eval(data['action'])        # Example: lambda block: print("Contract executed!")
    contract = SmartContract(data['name'], condition, action)

    blockchain.add_contract(contract)
    return jsonify({'message': 'Smart contract added successfully!'}), 201



if __name__ == '__main__':
    app.run(port=5000, debug=True)
