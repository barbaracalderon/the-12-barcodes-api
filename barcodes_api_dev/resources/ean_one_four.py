from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import EanOneFourController
from schemas import EanOneFourSchema

blp = Blueprint(
    "Barcode EAN-14",
    __name__,
    description="Turn 14 digits into an EAN-14 barcode. Accepts numeric characters.",
)


@blp.route("/ean-14")
class Barcode(MethodView):
    @blp.arguments(EanOneFourSchema)
    def post(self, barcode_data):
        ean_one_four_controller = EanOneFourController()
        response = ean_one_four_controller.create(barcode_data.get("product_number"))
        return response, 201
