from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask App 2 Alexa!!!! \n This is new flask app. \n Pretty cool! \n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')