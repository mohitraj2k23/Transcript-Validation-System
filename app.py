from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="Transcript Validator API", version="1.0")

ns = api.namespace("validate", description="Validation operations")

input_model = api.model("Input", {
    "transcript": fields.String(required=True, description="Input text")
})

@ns.route("/")
class Validate(Resource):
    @ns.expect(input_model)
    def post(self):
        data = api.payload
        text = data.get("transcript", "")

        if text.strip() == "":
            result = {"status": "Invalid", "reason": "Empty transcript"}
        elif len(set(text)) == 1:
            result = {"status": "Invalid", "reason": "Noise-only text"}
        else:
            result = {"status": "Valid", "reason": "Looks good"}

        return result

if __name__ == "__main__":
    app.run(debug=True)
