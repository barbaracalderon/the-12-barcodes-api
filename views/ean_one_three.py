from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import EanOneThreeController
from schemas import EanOneThreeSchema

blp = Blueprint(
    "Barcode EAN-13",
    __name__,
    description="Operations on barcode EAN-13.",
)


@blp.route("/ean-13")
class Barcode(MethodView):

    def __init__(self):
        self.ean_one_three_controller = EanOneThreeController()

    @blp.arguments(EanOneThreeSchema)
    def post(self, barcode_data):
        response, status_code = self.ean_one_three_controller.create(
            barcode_data.get("product_data")
        )
        return response, status_code

    def get(self):
        response = self.ean_one_three_controller.get_data()
        return response, 200
