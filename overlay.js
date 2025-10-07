const fetch = require("node-fetch");

async function runOverlay() {
  try {
    const status = await fetch("http://localhost:5000/status");
    const statusData = await status.json();
    console.log("Capsule Status:", statusData);

    const prediction = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input: "capsule test" })
    });
    const predictionData = await prediction.json();
    console.log("Prediction:", predictionData);
  } catch (error) {
    console.error("Overlay Error:", error);
  }
}

runOverlay();
