from blockchain import Blockchain
from flask import Flask, jsonify
from uuid import uuid4
from flask import request
import sys

app = Flask(__name__)
blockchain = Blockchain()
app_port=5000
receiver_default = 'Fernando'
node_adress = str(uuid4()).replace('-', '')



@app.route('/mine-block', methods=['GET'])
def mine():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    blockchain.add_transaction(
        sender=node_adress, receiver=receiver_default, amount=1)
    response = {'message': 'block minerado',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transaction': block['transactions']
                }
    return jsonify(response, 200)


@app.route('/get-blockchain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)
                }
    return jsonify(response)


@app.route('/blockchain-is-valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)

    return jsonify({'status': is_valid}, 200)


@app.route('/add-transaction', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_key = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_key):
        return 'Alguns elementos estao faltando', 400
    index = blockchain.add_transaction(
        json['sender'], json['receiver'], json['amount'])
    response = {'message': f'Esta transacao dera adicionado ao bloco {index}'}

    return jsonify(response, 201)


@app.route('/connect-node', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "Vazio", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'Todos o nos conectados, blockchain contem os seguintes nos:',
                'total_nodes': list(blockchain.nodes)}

    return jsonify(response, 201)


@app.route('/replace-chain', methods=['GET'])
def replace_chain():
    response = {}
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Os nos tinham cadeias diferentes então foi subistituída',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'Tudo certo não houve subistituição',
                    'new_chain': blockchain.chain}
    return jsonify(response, 200)



print(str(sys.argv))
if len(sys.argv):
    if len(sys.argv) > 1:
        app_port = int(sys.argv[1])
    if len(sys.argv) > 2:
        receiver_default = sys.argv[2]

app.run(host='0.0.0.0', port=app_port)
