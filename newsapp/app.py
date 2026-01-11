from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "9bf1b66d7f2b404c8ab15a34fef4e066"

@app.route("/")
def home():
    return jsonify({"status": "News API running"})

@app.route("/news")
def news():
    category = request.args.get("category", "general")

    url = (
        "https://newsapi.org/v2/top-headlines?"
        f"country=us&category={category}&apiKey={API_KEY}"
    )

    r = requests.get(url).json()
    return jsonify(r)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
