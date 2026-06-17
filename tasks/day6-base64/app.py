from flask import Flask
from pathlib import Path
import base64

app = Flask(__name__)

def flag():
    return Path("/opt/ctf/flag.txt").read_text(encoding="utf-8").strip()

@app.route("/")
def index():
    return """
    <h2>Day 6 - Encoded Path</h2>
    <p>Goal: Decode the clue and visit the decoded path.</p>
    <p>Clue: <a href="/encoded">/encoded</a></p>
    """

@app.route("/encoded")
def encoded():
    encoded_path = base64.b64encode(b"/secret/base64-path").decode()
    return f"<h2>Encoded clue</h2><pre>{encoded_path}</pre><p>Decode it.</p>"

@app.route("/secret/base64-path")
def secret():
    return flag()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
