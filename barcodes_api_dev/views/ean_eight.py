from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import EanEightController
from schemas import EanEightSchema

blp = Blueprint(
    "Barcode EAN-8",
    __name__,
    description="Operations on barcode EAN-8.",
)


@blp.route("/ean-8")
class Barcode(MethodView):
    @blp.arguments(EanEightSchema)
    def post(self, barcode_data):
        ean_eight_controller = EanEightController()
        response = ean_eight_controller.create(barcode_data.get("product_number"))
        return response, 201

    def get(self):
        ean_eight_controller = EanEightController()
        response = ean_eight_controller.get_data()
        return response, 200