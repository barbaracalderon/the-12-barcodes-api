from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import ThreeNineController
from schemas import ThreeNineSchema

blp = Blueprint(
    "Barcode Code-39",
    __name__,
    description="Operations on barcode Code-39.",
)


@blp.route("/code-39")
class Barcode(MethodView):

    def __init__(self):
        self.three_nine_controller = ThreeNineController()

    @blp.arguments(ThreeNineSchema)
    def post(self, barcode_data):
        response = self.three_nine_controller.create(barcode_data.get("product_name"))
        return response, 201

    def get(self):
        response = self.three_nine_controller.get_data()
        return response, 200
