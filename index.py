from app import create_app
from jsonschema import ValidationError
from flask import jsonify, make_response

app = create_app()

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        return make_response(
            jsonify({"msg": "Error", "code": 400, "datos": {str(error.description.message): "error"}}),
            400
        )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")