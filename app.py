from flask import Flask, jsonify
import secrets

app = Flask(__name__)

@app.route('/')
def home():
    return "Token Generator API"

@app.route('/generate-token', methods=['GET'])
def generate_token():
    token = str(secrets.randbelow(900000) + 100000)
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run()
