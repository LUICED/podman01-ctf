from flask import Flask, request
from pathlib import Path
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 8 - Weak File Viewer</h2>
    <p>Goal: Read a private file using the file viewer.</p>
    <p>Normal file: <a href="/viewer?file=welcome.txt">/viewer?file=welcome.txt</a></p>
    <p>Hint: The viewer joins your filename with the public folder.</p>
    """

@app.route("/viewer")
def viewer():
    name = request.args.get("file", "welcome.txt")
    target = os.path.join("/opt/ctf/public", name)

    try:
        content = Path(target).read_text(encoding="utf-8")
        return "<pre>" + content + "</pre>"
    except Exception as e:
        return f"<h2>File error</h2><pre>{type(e).__name__}: {e}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
