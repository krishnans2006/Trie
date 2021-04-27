from models import Trie
import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


def send_actions():
    print("Trie Actions:\n1 - View Trie\n2 - Add Key\n3 - Delete Key\n4 - Search for a Key (True or False)\n5 - Get Autocomplete")

def view():
    display = requests.get(os.getenv("DOMAIN") + "/display").json()
    print(display["Result"])

def add(value):
    display = requests.post(os.getenv("DOMAIN") + "/add", headers=headers, data={"key": value}).json()
    print(display["Result"])

def delete(value):
    display = requests.post(os.getenv("DOMAIN") + "/delete", headers=headers, data={"key": value}).json()
    print(display["Result"])

def search(value):
    display = requests.post(os.getenv("DOMAIN") + "/search", headers=headers, data={"key": value}).json()
    print(display["Result"])

def autocomplete(value):
    display = requests.post(os.getenv("DOMAIN") + "/autocomplete", headers=headers, data={"key": value}).json()
    print(display["Result"])

while True:
    send_actions()
    action = input("Action: ")
    if action == "1":
        view()
    elif action == "2":
        value = input("Value to add: ")
        add(value)
    elif action == "3":
        value = input("Value to delete: ")
        delete(value)
    elif action == "4":
        value = input("Value to search: ")
        search(value)
    elif action == "5":
        value = input("Value to find autocompletes for: ")
        autocomplete(value)