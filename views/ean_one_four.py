from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import EanOneFourController
from schemas import EanOneFourSchema

blp = Blueprint(
    "Barcode EAN-14",
    __name__,
    description="Operations on barcode EAN-14.",
)


@blp.route("/ean-14")
class Barcode(MethodView):

    def __init__(self):
        self.ean_one_four_controller = EanOneFourController()

    @blp.arguments(EanOneFourSchema)
    def post(self, barcode_data):
        response, status_code = self.ean_one_four_controller.create(
            barcode_data.get("product_data")
        )
        return response, status_code

    def get(self):
        response = self.ean_one_four_controller.get_data()
        return response, 200
