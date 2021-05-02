from flask import Flask, jsonify, request
from models import Trie

app = Flask(__name__)
trie = None

@app.before_first_request
def setup_trie():
    global trie
    trie = Trie()


@app.route('/')
def index():
    return jsonify({
        "Message": "Welcome to the Trie API!"
    })


@app.route("/display")
def display():
    global trie
    return jsonify({
        "Result": trie.display()
    })


@app.route("/add", methods=["POST"])
def add():
    global trie
    key = request.form.get("key")
    trie.add(key)
    return jsonify({
        "Result": "Success"
    })


@app.route("/delete", methods=["POST"])
def delete():
    global trie
    key = request.form.get("key")
    trie.delete(key)
    return jsonify({
        "Result": "Success"
    })


@app.route("/search", methods=["POST"])
def search():
    global trie
    key = request.form.get("key")
    response = trie.search(key)
    return jsonify({
        "Result": response
    })


@app.route("/autocomplete", methods=["POST"])
def autocomplete():
    global trie
    key = request.form.get("key")
    response = trie.autocomplete(key)
    return jsonify({
        "Result": response
    })


if __name__ == '__main__':
    app.run()
