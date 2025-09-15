from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    # Path to the JSON file
    file_path = os.path.join(os.path.dirname(__file__), 'data.json')
    
    # Read and return the data
    with open(file_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

