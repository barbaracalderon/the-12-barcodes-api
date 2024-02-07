from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import EanEightController
from schemas import EanEightSchema

blp = Blueprint(
    "Barcode EAN-8",
    __name__,
    description="Turn 8 digits into an EAN-8 barcode. Accepts numeric characters.",
)


@blp.route("/ean-8")
class Barcode(MethodView):
    @blp.arguments(EanEightSchema)
    def post(self, barcode_data):
        ean_eight_controller = EanEightController()
        response = ean_eight_controller.create(barcode_data.get("product_number"))
        return response, 201
