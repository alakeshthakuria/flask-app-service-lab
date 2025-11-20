from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():
    try:
        # Free public weather API (no API key required)
        url = "https://wttr.in/?format=j1"
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch weather data"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
