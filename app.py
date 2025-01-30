import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome all!"

@app.route('/how are you')
def hello():
    return 'I am very good, how about you?'

@app.route('/code')
def code_example():
    return '''
    ```python
    def greet(name):
        return f"Hello, {name}!"
    ```
    '''

@app.route('/code2')
def code_example2():
    return '''
    ```python
    def add(x, y):
        return x + y
    ```
    '''

@app.route('/code3')
def code_example3():
    return '''
    ```python
    def multiply(x, y):
        return x * y
    ```
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
