from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({"status": "ok", "device": "Samsung A13"})
