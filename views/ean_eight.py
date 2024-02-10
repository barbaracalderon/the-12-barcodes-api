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

    def __init__(self):
        self.ean_eight_controller = EanEightController()

    @blp.arguments(EanEightSchema)
    def post(self, barcode_data):
        response, status_code = self.ean_eight_controller.create(
            barcode_data.get("product_data")
        )
        return response, status_code

    def get(self):
        response = self.ean_eight_controller.get_data()
        return response, 200
