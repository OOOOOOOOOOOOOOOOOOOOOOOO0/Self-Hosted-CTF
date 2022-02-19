from flask import Flask, request, redirect
import json




# Code is down there incase you haven't completed the challenge :3

































































































app = Flask(__name__)
#app.config['DEBUG'] = True

with open('Answer/details.json', 'r') as fp:
    config = json.load(fp)

username = config['username']
password = config['password']
flag = config['flag']

@app.route('/', methods=['POST', 'GET'])
def index():
  return redirect('challenge')

@app.route('/challenge', methods=['POST', 'GET'])
def challenge():
  if request.method == 'POST' and request.form['username'] == username and request.form['password'] == password:
    return f"Congratulations! You completed the challenge, the flag is: {flag}\n\n\n\n\nIf you'd like to read the source code of this challenge: https://replit.com/@Argue/POST-CTF"
  else:
    return f"<title>CTF</title> <h1> Welcome to C0mpt0's POST Request CTF Challenge, this site takes <b>POST</b> data only, the challenge is to find the flag, goodluck </h1><!--- username: {username} | password: {password}, what can you do with this data?---!> <small> hint: fnhpr, i love rot13! </small>"

app.run(host="127.0.0.1", port=1337)
