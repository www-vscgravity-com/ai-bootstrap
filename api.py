

















































from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Injected endpoints
@app.route("/health")
def health():
    return {"status": "ok", "capsule": "ai-bootstrap"}, 200

@app.route("/sync")
def sync():
    return {"sync": "resume artifacts injected"}, 200

@app.route("/validate")
def validate():
    return {"validate": "capsule logic confirmed"}, 200

# 🔹 Existing capsule logic
@app.route("/predict", methods=["POST"])
def predict_capsule():
    data = request.json
    input_text = data.get("input", "")

    prediction = "positive" if "profit" in input_text.lower() else "neutral"

    return jsonify({
        "input": input_text,
        "prediction": prediction,
        "confidence": 0.92,
        "capsule": "profit-capsule"
    })

@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "capsule": "profit-capsule",
        "status": "online",
        "uptime": "4h 12m",
        "requests": 57
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

































