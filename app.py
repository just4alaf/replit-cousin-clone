from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Replit Cousin Clone – AI Agent Ready"

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == "__main__":
    port = int(os.getenv("PORT", '5000'))
    app.run(host="0.0.0.0", port=port, debug=True)
