from flask import Flask, render_template
from flask_smorest import Api
from views.one_two_eight import blp as OneTwoEightBlueprint
from views.upc_a import blp as UpcABlueprint
from views.three_nine import blp as ThreeNineBlueprint
from views.issn import blp as IssnBlueprint
from views.isbn_ten import blp as IsbnTenBlueprint
from views.isbn_one_three import blp as IsbnOneThreeBlueprint
from views.pzn_seven import blp as PznSevenBlueprint
from views.ean_one_three import blp as EanOneThreeBlueprint
from views.ean_eight import blp as EanEightBlueprint
from views.jan import blp as JanBlueprint
from views.ean_one_four import blp as EanOneFourBlueprint
from views.gs_one_one_two_eight import blp as GsOneOneTwoEightBlueprint


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def main():
        return render_template("index.html")
    

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "12 Barcodes API Dev"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    api = Api(app)

    api.register_blueprint(OneTwoEightBlueprint)
    api.register_blueprint(UpcABlueprint)
    api.register_blueprint(ThreeNineBlueprint)
    api.register_blueprint(IssnBlueprint)
    api.register_blueprint(IsbnTenBlueprint)
    api.register_blueprint(IsbnOneThreeBlueprint)
    api.register_blueprint(PznSevenBlueprint)
    api.register_blueprint(EanOneThreeBlueprint)
    api.register_blueprint(EanEightBlueprint)
    api.register_blueprint(JanBlueprint)
    api.register_blueprint(EanOneFourBlueprint)
    api.register_blueprint(GsOneOneTwoEightBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
