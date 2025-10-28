from flask import Flask, request, jsonify
from model import MODEL

app = Flask(__name__)
model = MODEL()

@app.route('/extract', methods=["POST"])
def extract():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing values"}), 400

    text = data["text"]
    results = model.analyze(text)
    return jsonify(results)
