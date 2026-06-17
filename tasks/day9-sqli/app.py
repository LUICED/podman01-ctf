from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 9 - Weak SQL Login</h2>
    <p>Goal: Login as admin.</p>
    <p>Try guest first:</p>
    <p><a href="/login?user=guest&pass=guest">/login?user=guest&amp;pass=guest</a></p>
    <p>Hint: The login query is intentionally weak for CTF practice.</p>
    """

@app.route("/login")
def login():
    user = request.args.get("user", "")
    password = request.args.get("pass", "")

    db = sqlite3.connect("/opt/ctf/app.db")
    cur = db.cursor()

    sql = f"SELECT username, role FROM users WHERE username = '{user}' AND password = '{password}'"

    try:
        row = cur.execute(sql).fetchone()
    except Exception as e:
        return f"""
        <h2>SQL Error</h2>
        <pre>{e}</pre>
        <p>Query was:</p>
        <pre>{sql}</pre>
        """

    if not row:
        return "<h2>Login failed</h2><p>No matching user.</p>"

    username, role = row

    if role == "admin":
        flag = cur.execute("SELECT value FROM secrets WHERE name='flag'").fetchone()[0]
        return f"<h2>Admin login success</h2><p>Welcome {username}</p><pre>{flag}</pre>"

    return f"""
    <h2>Guest login success</h2>
    <p>Welcome {username}. Role: {role}</p>
    <p>Only admin can see the flag.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
