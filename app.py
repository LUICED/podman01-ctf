from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Podman01 CTF - Day 1</h2>
    <p>Welcome to the first Docker CTF task.</p>
    <p>Goal: Find the flag.</p>
    <p>Hint: Check /robots.txt</p>
    """

@app.route("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /secret-flag\n"

@app.route("/secret-flag")
def flag():
    return "CTF{podman01_day1_basic_success}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
