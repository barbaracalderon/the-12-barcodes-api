from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import UpcAController
from schemas import UpcASchema

blp = Blueprint(
    "Barcode UPC-A",
    __name__,
    description="Operations on barcode UPC-A.",
)


@blp.route("/upc-a")
class Barcode(MethodView):

    def __init__(self):
        self.upc_a_controller = UpcAController()

    @blp.arguments(UpcASchema)
    def post(self, barcode_data):
        response, status_code = self.upc_a_controller.create(
            barcode_data.get("product_number")
        )
        return response, status_code

    def get(self):
        response = self.upc_a_controller.get_data()
        return response, 200
