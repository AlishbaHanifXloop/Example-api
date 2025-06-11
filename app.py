from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask API on Render!")

@app.route('/greet/<name>')
def greet(name):
    return jsonify(greeting=f"Hello, {name}!")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
