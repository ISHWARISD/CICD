"""
A tiny Flask app -- just enough to demonstrate CI/CD concepts.
Run locally with: python app.py
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello, Ish! This app is alive.")


@app.route("/health")
def health():
    """Used by deployment platforms to check if the app is running."""
    return jsonify(status="ok")


def add(a, b):
    """A simple function we can unit test."""
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
