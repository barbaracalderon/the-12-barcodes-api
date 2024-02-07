from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import OneTwoEightController
from schemas import OneTwoEightSchema

blp = Blueprint(
    "Barcode Code-128",
    __name__,
    description="Operations on barcode Code-128",
)


@blp.route("/code-128")
class Barcode(MethodView):
    @blp.arguments(OneTwoEightSchema)
    def post(self, barcode_data):
        one_two_eight_controller = OneTwoEightController()
        response = one_two_eight_controller.create(barcode_data.get("product_name"))
        return response, 201
