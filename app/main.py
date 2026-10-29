from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []


@app.route("/")
def home():
    return "To-Do API v2 is running"


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify(error="title is required"), 400
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    return jsonify(task), 201