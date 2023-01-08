from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

@app.route('/calculate', methods=['POST'])
def calculate():
    x = request.form['x']
    y = request.form['y']
    operation = request.form['operation']
    x = float(x)
    y = float(y)
    if operation == 'add':
        result = add(x, y)
    elif operation == 'subtract':
        result = subtract(x, y)
    elif operation == 'multiply':
        result = multiply(x, y)
    elif operation == 'divide':
        result = divide(x, y)
    else:
        result = 'Invalid operation'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
