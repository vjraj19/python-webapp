import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome all!"

@app.route('/how are you')
def hello():
    return 'I am nice, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
