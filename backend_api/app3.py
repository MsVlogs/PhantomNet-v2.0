# backend_api/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "PhantomNet API Running"})

@app.route("/logs")
def get_logs():
    if not os.path.exists("../phantomnet_agent/logs/attacks.log"):
        return jsonify({"logs": []})
    with open("../phantomnet_agent/logs/attacks.log") as f:
        logs = f.readlines()
    return jsonify({"logs": logs})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
