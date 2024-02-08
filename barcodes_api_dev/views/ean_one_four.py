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
    @blp.arguments(EanOneFourSchema)
    def post(self, barcode_data):
        ean_one_four_controller = EanOneFourController()
        response = ean_one_four_controller.create(barcode_data.get("product_number"))
        return response, 201

    def get(self):
        ean_one_four_controller = EanOneFourController()
        response = ean_one_four_controller.get_data()
        return response, 200