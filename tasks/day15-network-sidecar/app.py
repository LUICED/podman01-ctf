import os
import urllib.request
from flask import Flask
from pathlib import Path

ROLE = os.environ.get("ROLE", "app")
TOKEN_SERVICE = os.environ.get("TOKEN_SERVICE", "http://token-service:9090/token")
FLAG = Path("/opt/ctf/flag.txt")
TOKEN = "do188-network-ok"

app = Flask(__name__)

@app.route("/")
def index():
    if ROLE == "sidecar":
        return "<h2>Token sidecar</h2><p>Endpoint: /token</p>"

    try:
        with urllib.request.urlopen(TOKEN_SERVICE, timeout=2) as resp:
            token = resp.read().decode().strip()
    except Exception as e:
        return f"""
        <h2>Day 15 - Podman Network Sidecar</h2>
        <p>The app cannot reach the token service.</p>
        <p>Expected service URL: <code>{TOKEN_SERVICE}</code></p>
        <pre>{type(e).__name__}: {e}</pre>
        <p>Hint: run two containers on the same user-defined podman network.</p>
        """

    if token == TOKEN:
        return f"<h2>Network OK</h2><pre>{FLAG.read_text(encoding='utf-8').strip()}</pre>"

    return f"<h2>Wrong token</h2><pre>{token}</pre>"

@app.route("/token")
def token():
    if ROLE == "sidecar":
        return TOKEN
    return "This container is not the token sidecar", 404

if __name__ == "__main__":
    port = 9090 if ROLE == "sidecar" else 8080
    app.run(host="0.0.0.0", port=port)
