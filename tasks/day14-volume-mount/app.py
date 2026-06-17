from flask import Flask
from pathlib import Path

app = Flask(__name__)
UNLOCK = Path("/data/unlock.txt")
FLAG = Path("/opt/ctf/flag.txt")

@app.route("/")
def index():
    if not UNLOCK.exists():
        return """
        <h2>Day 14 - Volume Mount</h2>
        <p>No unlock file found at <code>/data/unlock.txt</code>.</p>
        <p>Create a host file and bind mount it into the container.</p>
        <p>Required content: <code>do188-volume-ok</code></p>
        """

    value = UNLOCK.read_text(encoding="utf-8").strip()
    if value == "do188-volume-ok":
        return f"<h2>Unlocked</h2><pre>{FLAG.read_text(encoding='utf-8').strip()}</pre>"

    return f"<h2>Wrong unlock value</h2><pre>{value}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
