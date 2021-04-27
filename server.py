from flask import Flask, jsonify, request
from models import Trie

app = Flask(__name__)
trie = Trie()
trie.add("a")
trie.add("b")
trie.add("at")
trie.add("al")
trie.add("alt")
trie.add("alte")
trie.add("alter")
trie.add("ate")
trie.add("ar")
trie.add("art")
trie.add("are")
trie.add("aren")
trie.add("arent")
trie.add("by")
trie.add("bye")
trie.add("bo")
trie.add("bol")
trie.add("bold")
trie.delete("alt")

@app.route('/')
def index():
    return jsonify({
        "Message": "Welcome to the Trie API!"
    })

@app.route("/display")
def display():
    return jsonify({
        "Result": trie.display()
    })

@app.route("/add", methods=["POST"])
def add():
    key = request.form.get("key")
    trie.add(key)
    return jsonify({
        "Result": "Success"
    })

@app.route("/delete", methods=["POST"])
def delete():
    key = request.form.get("key")
    trie.delete(key)
    return jsonify({
        "Result": "Success"
    })

@app.route("/search", methods=["POST"])
def search():
    key = request.form.get("key")
    response = trie.search(key)
    return jsonify({
        "Result": response
    })

@app.route("/autocomplete", methods=["POST"])
def autocomplete():
    key = request.form.get("key")
    response = trie.autocomplete(key)
    return jsonify({
        "Result": response
    })

if __name__ == '__main__':
    app.run()
