from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 13 - Image Layer History</h2>
    <p>The flag was added during build and deleted in a later layer.</p>
    <p>It is not available in the running container.</p>
    <p>Hint: container image layers can preserve data from earlier build steps.</p>
    <pre>podman history docker.io/luvsannorovv/podman01:day13-image-layer-history</pre>
    <p>Think about saving/exporting the image and inspecting layer tar files.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
