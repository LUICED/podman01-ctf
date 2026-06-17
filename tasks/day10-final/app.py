from flask import Flask, request, make_response
from pathlib import Path
import base64
import json

app = Flask(__name__)

def flag():
    return Path("/opt/ctf/flag.txt").read_text(encoding="utf-8").strip()

@app.route("/")
def index():
    return """
    <h2>Day 10 - Final Multi-step</h2>
    <p>Goal: Follow the trail and get the final flag.</p>
    <p>Hint: Start with common web discovery.</p>
    """

@app.route("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /backup.b64\n", 200, {"Content-Type": "text/plain"}

@app.route("/backup.b64")
def backup():
    data = {
        "next": "/stage2",
        "cookie_name": "stage",
        "cookie_value": "blue-team"
    }
    return base64.b64encode(json.dumps(data).encode()).decode(), 200, {"Content-Type": "text/plain"}

@app.route("/stage2")
def stage2():
    if request.cookies.get("stage") != "blue-team":
        return "<h2>Stage 2</h2><p>Missing required cookie.</p>"

    resp = make_response("""
    <h2>Stage 2 passed</h2>
    <p>Good. Final endpoint: <code>/final</code></p>
    <p>Look at the response header for the key.</p>
    """)
    resp.headers["X-Final-Key"] = "podman-final-key"
    return resp

@app.route("/final")
def final():
    if request.args.get("key") == "podman-final-key":
        return flag()

    return "<h2>Final</h2><p>Missing or wrong key.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
