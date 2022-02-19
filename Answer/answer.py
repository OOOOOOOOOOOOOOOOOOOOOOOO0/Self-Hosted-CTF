import requests

# The challenge was to use POST request data. The username and password returns the flag

URL = "https://post-ctf.argue.repl.co/challenge" # URL Variable

DATA = { # The username and password as seen in the source code
  "username": "cats",
  "password": "123456"
}

r = requests.post(URL, data=DATA) # The POST request including the URL the DATA

print(r.text) # Returning the code we get from the POST request
