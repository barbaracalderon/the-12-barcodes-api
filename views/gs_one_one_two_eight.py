from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import GsOneOneTwoEightController
from schemas import GsOneOneTwoEightSchema


blp = Blueprint(
    "Barcode GS1-128",
    __name__,
    description="Operations on barcode GS1-128.",
)


@blp.route("/gs1-128")
class Barcode(MethodView):

    def __init__(self):
        self.gs_one_one_two_controller = GsOneOneTwoEightController()

    @blp.arguments(GsOneOneTwoEightSchema)
    def post(self, barcode_data):
        response, status_code = self.gs_one_one_two_eight_controller.create(
            barcode_data.get("product_data")
        )
        return response, status_code

    def get(self):
        response = self.gs_one_one_two_eight_controller.get_data()
        return response, 200
