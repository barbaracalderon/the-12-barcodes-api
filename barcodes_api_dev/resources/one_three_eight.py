from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import OneThreeEightController
from schemas import OneThreeEightSchema

blp = Blueprint(
    "Barcode Code-138",
    __name__,
    description="Operations on barcode Code138",
)


@blp.route("/code-138")
class Barcode(MethodView):
    @blp.arguments(OneThreeEightSchema)
    def post(self, barcode_data):
        one_three_eight_controller = OneThreeEightController()
        response = one_three_eight_controller.create(barcode_data.get("product_name"))
        return response, 201
