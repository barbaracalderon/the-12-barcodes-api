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
    @blp.arguments(UpcASchema)
    def post(self, barcode_data):
        upc_a_controller = UpcAController()
        response = upc_a_controller.create(barcode_data.get("product_number"))
        return response, 201
