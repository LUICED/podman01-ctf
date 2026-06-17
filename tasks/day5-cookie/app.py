from flask import Flask, request, make_response
from pathlib import Path

app = Flask(__name__)

def flag():
    return Path("/opt/ctf/flag.txt").read_text(encoding="utf-8").strip()

@app.route("/")
def index():
    return """
    <h2>Day 5 - Cookie Role Check</h2>
    <p>Goal: Become admin.</p>
    <p>Start: <a href="/login">/login</a></p>
    <p>Then check: <a href="/dashboard">/dashboard</a></p>
    """

@app.route("/login")
def login():
    resp = make_response("""
    <h2>Logged in as guest</h2>
    <p>Your role cookie is set to guest.</p>
    <p>Open <a href="/dashboard">/dashboard</a>.</p>
    """)
    resp.set_cookie("role", "guest")
    return resp

@app.route("/dashboard")
def dashboard():
    role = request.cookies.get("role", "none")
    if role == "admin":
        return f"<h2>Admin dashboard</h2><pre>{flag()}</pre>"

    return f"""
    <h2>Guest dashboard</h2>
    <p>Your role is <b>{role}</b>.</p>
    <p>Only admin can see the flag.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
