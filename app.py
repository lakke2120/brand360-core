from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Brand360 Core Service Running"

@app.route("/status")
def status():
    return jsonify({
        "service": "Brand360 Core",
        "status": "running",
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run()
