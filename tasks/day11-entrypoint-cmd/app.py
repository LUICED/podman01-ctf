import sys
from flask import Flask

FLAG_PATH = "/opt/ctf/flag.txt"
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 11 - ENTRYPOINT vs CMD</h2>
    <p>This image has a fixed <b>ENTRYPOINT</b> and a default <b>CMD</b>.</p>
    <p>The default CMD starts this web server, but another runtime argument can reveal the flag.</p>
    <p>Hint: inspect the image config and override only the CMD part.</p>
    <pre>podman inspect docker.io/luvsannorovv/podman01:day11-entrypoint-cmd</pre>
    """

def reveal():
    with open(FLAG_PATH, "r", encoding="utf-8") as f:
        print(f.read().strip())

def help_text():
    print("Usage modes: serve | reveal")

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "serve"

    if mode == "serve":
        app.run(host="0.0.0.0", port=8080)
    elif mode == "reveal":
        reveal()
    else:
        help_text()
