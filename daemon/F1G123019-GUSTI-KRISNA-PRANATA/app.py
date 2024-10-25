from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is running as a daemon!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
