from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<p> {parameter}</p>'


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '<br>'.join(str(i) for i in range(parameter + 1))
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return '<p>Error: Division by zero.</p>'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Invalid operation. Use +, -, *, div, or %.</p>'

    return f'<p>{num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)