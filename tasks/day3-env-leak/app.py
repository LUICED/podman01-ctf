from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Day 3 - Debug Environment Leak</h2>
    <p>Goal: Find sensitive data exposed through debug functionality.</p>
    <p>Hint: Try <code>/debug</code>.</p>
    """

@app.route("/debug")
def debug():
    if request.args.get("show") != "env":
        return """
        <h2>Debug endpoint</h2>
        <p>Debug is enabled.</p>
        <p>Try adding <code>?show=env</code>.</p>
        """

    data = {
        "TASK_TAG": os.environ.get("TASK_TAG", ""),
        "PODMAN01_FLAG": os.environ.get("PODMAN01_FLAG", "")
    }

    return "<pre>" + json.dumps(data, indent=2) + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
