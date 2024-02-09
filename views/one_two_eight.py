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

    def __init__(self):
        self.one_two_eight_controller = OneTwoEightController()

    @blp.arguments(OneTwoEightSchema)
    def post(self, barcode_data):
        response, status_code = self.one_two_eight_controller.create(
            barcode_data.get("product_name")
        )
        return response, status_code

    def get(self):
        response = self.one_two_eight_controller.get_data()
        return response, 200
