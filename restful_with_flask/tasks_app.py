from flask import Flask, jsonify

app = Flask(__name__)
HOST = "127.0.0.1"
PORT = 5000

tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit, Tyleno",
        "done": False
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "Need to find a good Python tutorial on the Web",
        "done": False
    }
]

@app.route("/todo/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
