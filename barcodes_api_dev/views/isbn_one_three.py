from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import IsbnOneThreeController
from schemas import IsbnOneThreeSchema

blp = Blueprint(
    "Barcode ISBN-13",
    __name__,
    description="Operations on barcode ISBN-13.",
)


@blp.route("/isbn-13")
class Barcode(MethodView):
    @blp.arguments(IsbnOneThreeSchema)
    def post(self, barcode_data):
        isbn_one_three_controller = IsbnOneThreeController()
        response = isbn_one_three_controller.create(barcode_data.get("product_code"))
        return response, 201
