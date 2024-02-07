from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import UpcController
from schemas import UpcSchema

blp = Blueprint("Barcode UPC-A", __name__, description="Turn 11 numbers into an UPC-A barcode. Accepts numeric characters.")

@blp.route("/upc")
class Barcode(MethodView):
    @blp.arguments(UpcSchema)
    def post(self, barcode_data):
        upc_controller = UpcController()
        response = upc_controller.create(barcode_data.get("product_number"))
        return response, 201