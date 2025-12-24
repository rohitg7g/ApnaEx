
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "ApnaEx server is running",
        "platform": "Render"
    })

@app.route("/health")
def health():
    return "OK", 200

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
