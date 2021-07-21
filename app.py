import json
from blockchain import Blockchain
from flask import Flask, jsonify


app = Flask(__name__)
blockchain = Blockchain()

print('ok')


@app.route('/mine-block', methods=['GET'])
def mine():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message': 'block minerado',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']
                }
    return jsonify(response, 200)


@app.route('/get-blockchain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)
                }
    return jsonify(response, 200)


@app.route('/blockchain-is-valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)

    return jsonify({'status':is_valid}, 200)


app.run(host='0.0.0.0', port=5000)
