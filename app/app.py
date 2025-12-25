from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Simple in-memory storage for demo purposes
tasks = [
    {"id": 1, "title": "Learn DevOps", "description": "Master CI/CD pipelines", "done": False},
    {"id": 2, "title": "Build Project", "description": "Create a working DevOps project", "done": False}
]

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({"error": "Title is required"}), 400
    task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
