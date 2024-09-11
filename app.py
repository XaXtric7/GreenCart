from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import hashlib
import json
from time import time

app = Flask(__name__)

# Enable CORS for all routes and all origins
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="project"
)

# Blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.new_block(previous_hash='1', proof=100)  # Create genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_data = []
        self.chain.append(block)
        return block

    def new_data(self, data):
        self.current_data.append(data)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

blockchain = Blockchain()

# Route to accept form data and create a block for contributions
@app.route('/contribute', methods=['POST'])
def contribute():
    data = request.json

    # Insert data into MySQL
    cursor = db.cursor()
    cursor.execute("INSERT INTO contributions (firstName, lastName, email, phone, address, energyType, energyUnits, frequency) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (data['firstName'], data['lastName'], data['email'], data['phone'], data['address'], data['energyType'], data['energyUnits'], data['frequency']))
    db.commit()

    # Create a new block with this data
    blockchain.new_data(data)
    block = blockchain.new_block(proof=123)

    response = {
        'message': 'New block has been added to the blockchain!',
        'block': block
    }
    return jsonify(response), 200

# Route to accept form data and create a block for energy purchases
@app.route('/buy', methods=['POST'])
def buy_energy():
    data = request.json
    energy_type = data['type']
    requested_amount = data['amount']

    # Check available energy from the contributions table
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT SUM(energyUnits) as total_energy FROM contributions WHERE energyType = %s", (energy_type,))
    result = cursor.fetchone()

    available_energy = result['total_energy'] if result['total_energy'] is not None else 0

    # Check if the requested amount exceeds the available energy
    if requested_amount > available_energy:
        return jsonify({'error': 'The requested quantity exceeds the available energy for this type.'}), 400

    # Insert data into purchases table if quantity is valid
    cursor.execute("INSERT INTO purchases (type, amount, total, name, email, address, city, state, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (data['type'], data['amount'], data['total'], data['name'], data['email'], data['address'], data['city'], data['state'], data['zipcode']))
    db.commit()

    # Create a new block with this purchase data
    blockchain.new_data(data)
    block = blockchain.new_block(proof=123)

    response = {
        'message': 'Purchase has been recorded and added to the blockchain!',
        'block': block
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
