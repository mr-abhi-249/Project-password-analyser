from flask import Flask, request, jsonify, send_from_directory
from analyzer import analyze_password
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "password" not in data:
        return jsonify({"error": "Password is required"}), 400

    password = data["password"]

    result = analyze_password(password)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)