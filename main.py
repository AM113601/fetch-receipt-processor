from flask import Flask, request, jsonify
import uuid
from rules import *

app = Flask(__name__)
data = {}

# Path: /receipts/process
# Method: POST
# Payload: Receipt JSON
# Response: JSON containing an id for the receipt.
@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    try:
        receipt_data = request.json
        id = str(uuid.uuid4()) # random id generated, unique identifier
        points = calculate_points(receipt_data)
        data[id] = points
        return jsonify({"id": id}), 200
    except: # bad formatted request
        return jsonify({"error": "Badly formatted JSON"}), 400

# Path: /receipts/{id}/points
# Method: GET
# Response: Json object containing number of points awarded.
@app.route('/receipts/<string:id>/points', methods=['GET'])
def get_points(id):
    if id in data:
        return jsonify({"points": data[id]}), 200
    return jsonify({"error": "Receipt not found"}), 404

# Run file
if __name__ == '__main__':
    app.run()