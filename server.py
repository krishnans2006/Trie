from flask import Flask, jsonify, request
from models import Trie

app = Flask(__name__)
trie = None


# Sets up the global trie
@app.before_first_request
def setup_trie():
    global trie
    trie = Trie()


# Displays a welcome message
@app.route('/')
def index():
    return jsonify({
        "Message": "Welcome to the Trie API!"
    })


# Displays the Trie
@app.route("/display")
def display():
    global trie
    return jsonify({
        "Result": trie.display()
    })


# Adds a key to the Trie
@app.route("/add", methods=["POST"])
def add():
    global trie
    key = request.form.get("key")
    if trie.add(key):
        return jsonify({
            "Result": f"Successfully added key '{key}'!"
        })
    else:
        return jsonify({
            "Result": "Please enter a string of letters!"
        })


# Deletes a key from the Trie
@app.route("/delete", methods=["POST"])
def delete():
    global trie
    key = request.form.get("key")
    if trie.delete(key):
        return jsonify({
            "Result": f"Successfully deleted key '{key}'!"
        })
    else:
        return jsonify({
            "Result": "This key does not exist! Please check your spelling or choose a valid key to delete."
        })


# Searches for a key in the Trie
@app.route("/search", methods=["POST"])
def search():
    global trie
    key = request.form.get("key")
    response = trie.search(key)
    return jsonify({
        "Result": response
    })


# Returns autocomplete suggestions using the Trie
@app.route("/autocomplete", methods=["POST"])
def autocomplete():
    global trie
    key = request.form.get("key")
    response = trie.autocomplete(key)
    if response[0]:
        return jsonify({
            "Result": response[1]
        })
    else:
        return jsonify({
            "Result": ["Invalid key! Please enter a valid string to find autocomplete suggestions for."]
        })


# For debugging purposes, and to run a version of the server on your computer if you want
if __name__ == '__main__':
    app.run()
