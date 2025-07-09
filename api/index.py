from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React

@app.route("/api")
def hello():
    return jsonify({"message": "Flask API connected - React + Vercel ready!"})

if __name__ == "__main__":
    app.run(debug=True)
