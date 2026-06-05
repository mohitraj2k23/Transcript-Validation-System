from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Transcript Validator API is running 🚀"

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    text = data.get("transcript", "")

    # Simple validation logic
    if text.strip() == "":
        result = {"status": "Invalid", "reason": "Empty transcript"}
    elif len(set(text)) == 1:
        result = {"status": "Invalid", "reason": "Noise-only text"}
    else:
        result = {"status": "Valid", "reason": "Looks good"}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
