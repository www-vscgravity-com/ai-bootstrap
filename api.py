from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict_capsule():
    data = request.json
    input_text = data.get("input", "")
    
    # Mock AI logic
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
    app.run(port=5000)
