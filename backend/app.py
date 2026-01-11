from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Връзка към MongoDB чрез името на Service в K8s
mongo_url = os.getenv("MONGO_URL", "mongodb://db:27017")
client = MongoClient(mongo_url)
db = client.notes_db

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(db.tasks.find({}, {'_id': 0}))
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if data and 'title' in data:
        db.tasks.insert_one({"title": data['title']})
        return jsonify({"status": "Task added"}), 201
    return jsonify({"error": "Invalid data"}), 400

@app.route('/tasks', methods=['DELETE'])
def delete_tasks():
    db.tasks.delete_many({})
    return jsonify({"status": "All tasks deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)