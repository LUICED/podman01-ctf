from flask import Flask, send_file
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 12 - ARG at build time</h2>
    <p>This is a build-focused challenge.</p>
    <p>Download the starter project and build it with the correct build argument.</p>
    <p>Download: <a href='/starter.tar.gz'>/starter.tar.gz</a></p>
    <p>Hint: read the Containerfile carefully. ARG exists during build, not necessarily at runtime.</p>
    """

@app.route("/starter.tar.gz")
def starter():
    return send_file("/opt/challenge/starter.tar.gz", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
