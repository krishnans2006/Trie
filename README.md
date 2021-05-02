# Trie

## Description
This is a REST API and Command-Line Interface (CLI) used to access, store, and modify keys in a Trie.

## The Process
The only major part of the project which I had experience with was the Flask REST API.
The rest was all out of my comfort zone.  

After making the basic API and CLI, I originally thought of deploying the server to Heroku.
I had experience using Heroku, and it works just as well as other hosting services.
However, I was mistaken. 
Heroku had many limitations, like that it does not support global states and that requests are not processed in the order that they are received in.
This meant I had to attempt using another Cloud Service, such as AWS or GCP. 
It took a lot of hard work, and after figuring out a lot of things, I finally deployed the server to AWS.
As a relief, the global state worked, and requests were processed correctly too.
It felt amazing, since I had never done it before and had finally figured it out.  

There were some other major issues that I faced during the process of coding this (which is why it took so long).
For example, my computer started experiencing random slowness, and apps kept crashing.
I had to completely wipe and reset my computer to fix this issue.
However, after the wipe, the available RAM on my computer felt so small, so when I had both a browser tab and my IDE open, the browser tabs would not load due to not enough memory.
All these issues were very frustrating, but I perservered through them to make a working server, client, and model that works perfectly!

I really enjoyed this challenge, because of many reasons. 
It was a perfect mix of what I did know and what I didn't know, which made it very challenging but fun at the same time.
Plus, having a due date for the project made me focus and work hard to finish it before the deadline.
I hope you enjoy using the Trie!

## Server
### REST API
The REST API can be found [here](http://flask-env.eba-pxjvpazg.us-east-2.elasticbeanstalk.com/). 
This API is a Flask webserver, hosted on [AWS](https://aws.amazon.com/) (Amazon Web Services) 
using [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).
The source code for the server can be found in the `server.py` file.  

The server contains many endpoints, which can be used to access and modify the Trie.
The Homepage (which contains a welcome message to the API) and the Display page can be accessed using a GET request.
The Add, Delete, Search, and Autocomplete endpoints will be accessed using a POST request, with the necessary data provided in the `x-www-form-urlencoded` format.
The data required is a value called `key`, with the string of characters to add, delete, search, or autocomplete for.
The server can be tested using curl, by curling to this URL: http://flask-env.eba-pxjvpazg.us-east-2.elasticbeanstalk.com/

The server contains one Trie, stored in a global state. All endpoints will either access or update this Trie. 
Additionally, the webserver is not threaded, which means requests will be processed in the order they are received.

## Client
### Command-Line Interface
The Command-Line Interface can be accessed by running the `client.py` file.
First, download or clone the repository to your computer.
Then, run the `client.py` file to load the CLI Interface!  
> Note: You will need Python 3.x installed in order to run the CLI.

The client allows the user to perform 5 actions, namely to display the trie, add an element, delete an element, search for an element, and to get autocomplete suggestions.
The client also allows users to quit the CLI.

All the Trie-related actions send GET or POST requests to the server, hosted on AWS.

## Unit Tests
The Unit Tests for the Trie were written using the `unittest` module in Python. 
Two unit tests were created, which check the validity of JSON responses, the global state of the Trie, and order of processing requests.

### Validity Test
This test runs every function possible, to make sure that the JSON responses returned are valid.
Additionally, it makes sure no change was made to the global Trie at the end of the test.

### Global State Test
This test adds an element to the global Trie and then immediately searches to make sure the element was added.
This makes sure that the new element is present during the second request (made individually), immediately after it was added.
Additionally, it makes sure to remove the newly added element so that no change is made to the global Trie at the end of the test.

### Processing Order Test
The order of processing requests is tested on both the Validity Test and the Global State Test.
In the validity test, the search and autocomplete are checked right after the given string is added to the Trie, and right before it is removed.
The validity test makes sure that the search and autocomplete functions return True and an empty list, respectively.
Additionally, the Global State Test does something similar, and will not work when requests are processed asynchronously.

## Model
The model for the Trie uses two Python Classes - `class Trie` and `class TrieElement`. 

### Class Trie
The Trie class is a class that stores the starting element of a trie (a `TrieElement`) and includes multiple helpful methods.

 - The `add` method 
    - Uses a string of characters to add a new key at a certain location in the Trie
    - It will use all the letters except the last letter in order to locate where to add the new key
    - If any of these letters don't exist, it will add them too
    - Finally, it will add a key with the value of the last letter, in the position where it is supposed to go
 - The `delete` method
    - Uses a string of characters to remove a key at a certain location in the Trie
    - It will use all the letters except the last letter in order to locate which key to remove
    - If any of these keys don't exist, it will not remove any key
    - If it can locate exactly where the key is located, it will remove it from the Trie
    - If the key to be removed has any children, they will be deleted as well
    - This purposefully does not delete the entire word, and only deletes the key at the end of the word
    - This is in order to preserve other words that may be formed using the keys
 - The `search` method
    - Uses a string of characters to locate a key in the Trie
    - Returns `True` if the key at that location is present
    - Returns `False` if the key at that location is not present
 - The `autocomplete` method
    - Uses a string of characters to generate possible options moving deeper into the Trie
    - For example, if the current element has 3 children: `a`, `e`, and `n`, these will be displayed as autocomplete suggestions
 - The `display` method
    - Uses many spaces and newlines to provide a visual representation of the Trie
    - Combines keys with only one child into a single line
    - Expands keys with multiple children into multiple lines and shows the branching point
    - Sample output:  
```
h i
  a l o
      t
  e l l o
    a t
```
This would be generated by adding: `hi`, `halo`, `halt`, `hello`, and `heat` to the Trie.       

### Class TrieElement
The `TrieElement` class stores the attributes of a single element or key in a Trie.
 - The `name` attribute
     - Stores the letter key of the element
 - The `parent` attribute
    - Contains a link to a `TrieElement` which is the parent of this TrieElement
 - The `children` attribute
    - Contains a list of `TrieElement` children who are the children of this TrieElement
 - The `add` method
    - Adds a child `TrieElement` to the current TrieElement, given a name
 - The `delete` method
    - Removes a child `TrieElement` from the current TrieElement, given a name, if it exists
 - The `next` method
    - If given a key, it returns the `TrieElement` object of the child with the given key, if it exists
    - If not given a key, it returns all the children of the current TrieElement
