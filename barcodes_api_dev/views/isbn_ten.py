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
    @blp.arguments(IsbnTenSchema)
    def post(self, barcode_data):
        isbn_ten_controller = IsbnTenController()
        response = isbn_ten_controller.create(barcode_data.get("product_code"))
        return response, 201
