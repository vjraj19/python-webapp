import os
from flask import Flask, request, jsonify

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
    python
    def greet(name):
        return f"Hello, {name}!"
    
    '''

@app.route('/code2')
def code_example2():
    return '''
    python
    def add(x, y):
        return x + y
    
    '''

@app.route('/code3')
def code_example3():
    return '''
    python
    def multiply(x, y):
        return x * y
    
    '''

@app.route('/post', methods=['POST'])
def post_example():
    name = request.form.get('name', '').strip()
    
    if not name:
        return 'Please provide a name.', 400
    if not name.isalpha():
        return 'Please provide a valid name.', 400
    
    return f'Hello {name}!'

@app.route('/get', methods=['GET'])
def get_example():
    name = request.args.get('name', '').strip()

    if not name:
        return 'Please provide a name.', 400
    if not name.isalpha():
        return 'Please provide a valid name.', 400
    
    return f'Hello {name}!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
