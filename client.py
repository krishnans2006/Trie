import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Sends values in the correct format
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


# Sends the actions message
def send_actions():
    print(
        "Trie Actions:\n1 - View Trie\n2 - Add Key\n3 - Delete Key\n4 - Search for a Key (True or False)\n5 - Get Autocomplete\n6 - Quit")


# Functions to send requests to the API and provide data
def view():
    display = requests.get(os.getenv("DOMAIN") + "/display").json()
    try:
        print(display["Result"])
    except:
        print("Sorry, an error occurred. Please try again!")


def add(value):
    display = requests.post(os.getenv("DOMAIN") + "/add", headers=headers, data={"key": value}).json()
    try:
        print(display["Result"])
    except:
        print("Sorry, an error occurred. Please try again!")


def delete(value):
    display = requests.post(os.getenv("DOMAIN") + "/delete", headers=headers, data={"key": value}).json()
    try:
        print(display["Result"])
    except:
        print("Sorry, an error occurred. Please try again!")


def search(value):
    display = requests.post(os.getenv("DOMAIN") + "/search", headers=headers, data={"key": value}).json()
    try:
        print(display["Result"])
    except:
        print("Sorry, an error occurred. Please try again!")


def autocomplete(value):
    display = requests.post(os.getenv("DOMAIN") + "/autocomplete", headers=headers, data={"key": value}).json()
    try:
        print("Your Autocomplete Suggestions:\n", ", ".join(display["Result"]))
    except:
        print("Sorry, an error occurred. Please try again!")


# Runs when the file is executed
while True:  # Repeats until quit
    send_actions()
    action = input("Action: ")
    try:
        action = int(action)
    except:
        print("Please enter a valid action!")
        continue
    if action == 1:
        view()
    elif action == 2:
        value = input("Value to add: ")
        add(value)
    elif action == 3:
        value = input("Value to delete: ")
        delete(value)
    elif action == 4:
        value = input("Value to search: ")
        search(value)
    elif action == 5:
        value = input("Value to find autocompletes for: ")
        autocomplete(value)
    elif action == 6:
        print("We hope you enjoyed using the Trie API!")
        break
    else:
        print("Please enter a valid action number!")
        continue
