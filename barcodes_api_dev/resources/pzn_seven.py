from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import PznSevenController
from schemas import PznSevenSchema

blp = Blueprint(
    "Barcode PZN7",
    __name__,
    description="Turn strings into a PZN7 barcode. Accepts 7 numeric characters.",
)


@blp.route("/pzn7")
class Barcode(MethodView):
    @blp.arguments(PznSevenSchema)
    def post(self, barcode_data):
        pzn_seven_controller = PznSevenController()
        response = pzn_seven_controller.create(barcode_data.get("product_number"))
        return response, 201
