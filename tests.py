import unittest
import requests
import os

# Sends values in the correct format
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Sets the domain
DOMAIN = os.getenv("DOMAIN", default="http://flask-env.eba-pxjvpazg.us-east-2.elasticbeanstalk.com/")


# The Unit Test for the Trie
class TestTrie(unittest.TestCase):
    def test_errors(self):
        # Make sure all endpoints return valid json responses
        self.assertIsNotNone(requests.get(DOMAIN + "/display").json().get("Result"))
        self.assertIsNotNone(
            requests.post(DOMAIN + "/add", headers=headers, data={"key": "atest"}).json().get("Result"))
        self.assertIsNotNone(
            requests.post(DOMAIN + "/search", headers=headers, data={"key": "atest"}).json().get("Result"))
        self.assertNotEqual(
            requests.post(DOMAIN + "/autocomplete", headers=headers, data={"key": "atest"}).json().get("Result"),
            ["Invalid key! Please enter a valid string to find autocomplete suggestions for."])
        self.assertIsNotNone(
            requests.post(DOMAIN + "/delete", headers=headers, data={"key": "atest"}).json().get("Result"))

    def test_global_state(self):
        # Adding the string to the Trie
        requests.post(DOMAIN + "/add", headers=headers, data={"key": "thisisatest"})

        # Asserting to see if it exists
        self.assertTrue(
            requests.post(DOMAIN + "/search", headers=headers, data={"key": "thisisatest"}).json()["Result"],
            "The key should exist when searching, since it was added")

        # Deleting the added string to not make an impact on the global Trie
        requests.post(DOMAIN + "/delete", headers=headers, data={"key": "thisisatest"})


if __name__ == "__main__":
    unittest.main()
