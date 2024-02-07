from flask import Flask, request, jsonify
from flask_smorest import Api
# from resources.one_three_eight import blp as BarcodeBlueprint
from resources.one_three_eight import blp as OneThreeEightBlueprint

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Barcodes API Dev"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    api = Api(app)

    api.register_blueprint(OneThreeEightBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
