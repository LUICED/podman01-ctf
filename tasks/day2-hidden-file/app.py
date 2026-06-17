from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 2 - Hidden File in Container</h2>
    <p>This web page does not directly show the flag.</p>
    <p>Open a terminal inside the container and search under <code>/opt/ctf</code>.</p>
    <p>Hint command: <code>find /opt/ctf -name '*flag*' 2&gt;/dev/null</code></p>
    """

@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
