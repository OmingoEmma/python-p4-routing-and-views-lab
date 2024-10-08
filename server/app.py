#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>', methods=['GET'])
def print_string(parameter):
    print(parameter)  
    return parameter  

@app.route('/count/<int:parameter>', methods=['GET'])
def count(parameter):

    numbers = "\n".join(str(i) for i in range(parameter))  it
    return Response(numbers, mimetype='text/plain')  

@app.route('/math/<int:num1>/<operation>/<int:num2>', methods=['GET'])
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero is not allowed.', 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation.', 400

    return str(result)  # Return the result as plain text

if __name__ == '__main__':
    app.run(port=5555, debug=True)

