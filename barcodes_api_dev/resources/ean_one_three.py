from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import EanOneThreeController
from schemas import EanOneThreeSchema

blp = Blueprint(
    "Barcode EAN-13",
    __name__,
    description="Turn 13 digits into an EAN-13 barcode. Accepts numeric characters.",
)


@blp.route("/ean-13")
class Barcode(MethodView):
    @blp.arguments(EanOneThreeSchema)
    def post(self, barcode_data):
        ean_one_three_controller = EanOneThreeController()
        response = ean_one_three_controller.create(barcode_data.get("product_number"))
        return response, 201
