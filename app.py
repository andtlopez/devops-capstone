from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World. Are you doing fine?'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)