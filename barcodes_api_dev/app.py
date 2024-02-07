from flask import Flask, request, jsonify
from flask_smorest import Api
from resources.one_three_eight import blp as OneThreeEightBlueprint
from resources.upc import blp as UpcBlueprint
from resources.three_nine import blp as ThreeNineBlueprint
from resources.issn import blp as IssnBlueprint
from resources.isbn_ten import blp as IsbnTenBlueprint
from resources.isbn_one_three import blp as IsbnOneThreeBlueprint
from resources.pzn_seven import blp as PznSevenBlueprint
from resources.ean_one_three import blp as EanOneThreeBlueprint


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
    api.register_blueprint(UpcBlueprint)
    api.register_blueprint(ThreeNineBlueprint)
    api.register_blueprint(IssnBlueprint)
    api.register_blueprint(IsbnTenBlueprint)
    api.register_blueprint(IsbnOneThreeBlueprint)
    api.register_blueprint(PznSevenBlueprint)
    api.register_blueprint(EanOneThreeBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
