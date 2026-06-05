from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app, title="Transcript Validator API", version="1.0")

ns = api.namespace("validate", description="Validation operations")

# Input model
input_model = api.model("Input", {
    "transcript": fields.String(required=True, description="Input text")
})

# 🔥 NEW: Smart validation function
def analyze_text(text):
    text = text.strip()

    if text == "":
        return {
            "status": "Invalid",
            "reason": "Empty transcript",
            "confidence": 0
        }

    unique_chars = len(set(text))
    length = len(text)

    score = (unique_chars / length) * 100

    if score < 20:
        return {
            "status": "Invalid",
            "reason": "Noise-only text",
            "confidence": round(score, 2)
        }
    elif score < 50:
        return {
            "status": "Suspicious",
            "reason": "Possibly noisy",
            "confidence": round(score, 2)
        }
    else:
        return {
            "status": "Valid",
            "reason": "Looks good",
            "confidence": round(score, 2)
        }

# API endpoint
@ns.route("/")
class Validate(Resource):
    @ns.expect(input_model)
    def post(self):
        data = api.payload
        text = data.get("transcript", "")

        # 👇 USE the function here
        result = analyze_text(text)

        return result

if __name__ == "__main__":
    app.run(debug=True)
