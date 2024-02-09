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

    def __init__(self):
        self.isbn_one_three_controller = IsbnOneThreeController()

    @blp.arguments(IsbnOneThreeSchema)
    def post(self, barcode_data):
        response, status_code = self.isbn_one_three_controller.create(
            barcode_data.get("product_code")
        )
        return response, status_code

    def get(self):
        response = self.isbn_one_three_controller.get_data()
        return response, 200
