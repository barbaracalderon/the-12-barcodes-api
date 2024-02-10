from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import IsbnTenController
from schemas import IsbnTenSchema

blp = Blueprint(
    "Barcode ISBN-10",
    __name__,
    description="Operations on barcode ISBN-10.",
)


@blp.route("/isbn-10")
class Barcode(MethodView):

    def __init__(self):
        self.isbn_ten_controller = IsbnTenController()

    @blp.arguments(IsbnTenSchema)
    def post(self, barcode_data):
        response, status_code = self.isbn_ten_controller.create(
            barcode_data.get("product_data")
        )
        return response, status_code

    def get(self):
        response = self.isbn_ten_controller.get_data()
        return response, 200
