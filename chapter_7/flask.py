# this shows comparsion between FastAPI and Flask, check fastapi.py file

from flask import Flask, jsonify, request

app = Flask(__name__)


# Path
@app.route("/hi/<who>", methods=["GET"])
def greet(who: str):
    return jsonify(f"Hello {who}")


# Query Parameter
@app.route("/hi", methods=["GET"])
def greet2():
    who: str = request.args.get("who")
    return jsonify(f"Hello {who}")


# Body
@app.route("/hi", methods=["GET"])
def greet3():
    who: str = request.json["who"]
    return jsonify(f"Hello {who}")


# Header
@app.route("/hi", methods=["GET"])
def greet4():
    who: str = request.headers.get("who")
    return jsonify(f"Hello {who}")
