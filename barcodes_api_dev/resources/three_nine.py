from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import ThreeNineController
from schemas import ThreeNineSchema

blp = Blueprint(
    "Barcode Code-39",
    __name__,
    description="Operations on barcode Code-39.",
)


@blp.route("/39")
class Barcode(MethodView):
    @blp.arguments(ThreeNineSchema)
    def post(self, barcode_data):
        three_nine_controller = ThreeNineController()
        response = three_nine_controller.create(barcode_data.get("product_name"))
        return response, 201
