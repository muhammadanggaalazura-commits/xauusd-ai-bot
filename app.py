from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "XAUUSD AI Bot server is running"
    })

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}

    print("Data diterima:", data)

    return jsonify({
        "status": "success",
        "message": "Webhook berhasil diterima"
    }), 200
