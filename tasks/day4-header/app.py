from flask import Flask, request, make_response
from pathlib import Path

app = Flask(__name__)

def flag():
    return Path("/opt/ctf/flag.txt").read_text(encoding="utf-8").strip()

@app.route("/")
def index():
    resp = make_response("""
    <h2>Day 4 - Header Based Access</h2>
    <p>Goal: Access <code>/api/flag</code>.</p>
    <p>Hint: Inspect HTTP response headers from this page.</p>
    """)
    resp.headers["X-CTF-Hint"] = "Use header X-CTF-Token: open-sesame"
    return resp

@app.route("/api/flag")
def api_flag():
    if request.headers.get("X-CTF-Token") == "open-sesame":
        return {"status": "ok", "flag": flag()}

    return {"status": "denied", "hint": "Missing or incorrect X-CTF-Token header"}, 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
