from flask import Flask, render_template

app = Flask(__name__)

@app.route('check_even_odd/<int:number>')
def check_even_odd(number):
    if number % 2 == 0:
        return f'The number {number} is even.'
    else:
        return f'The number (number} is odd.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')