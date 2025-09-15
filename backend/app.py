from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection (replace with your own Mongo URI if needed)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["todo_db"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get('itemName')
    item_desc = data.get('itemDescription')
    collection.insert_one({"name": item_name, "description": item_desc})
    return jsonify({"message": "Data submitted successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

