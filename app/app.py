from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Kestrel!"


@app.route("/health")
def health():
    return {"status": "ok"}
