from flask import Flask
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 7 - Linux Permission Misconfiguration</h2>
    <p>The web app cannot read the restricted flag file.</p>
    <p>Try: <a href="/read-restricted-flag">/read-restricted-flag</a></p>
    <p>Hint: Open a shell inside the container and search carefully under <code>/opt/ctf</code>.</p>
    """

@app.route("/read-restricted-flag")
def read_restricted_flag():
    try:
        return Path("/opt/ctf/restricted/flag.txt").read_text(encoding="utf-8")
    except Exception as e:
        return f"""
        <h2>Permission denied</h2>
        <p>The app user cannot read <code>/opt/ctf/restricted/flag.txt</code>.</p>
        <pre>{type(e).__name__}: {e}</pre>
        <p>Hint: A readable backup may exist.</p>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
