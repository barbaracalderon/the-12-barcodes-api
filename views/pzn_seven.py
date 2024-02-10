from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import PznSevenController
from schemas import PznSevenSchema

blp = Blueprint(
    "Barcode PZN7",
    __name__,
    description="Operations on barcode PZN7.",
)


@blp.route("/pzn7")
class Barcode(MethodView):

    def __init__(self):
        self.pzn_seven_controller = PznSevenController()

    @blp.arguments(PznSevenSchema)
    def post(self, barcode_data):
        response, status_code = self.pzn_seven_controller.create(
            barcode_data.get("product_data")
        )
        return response, status_code

    def get(self):
        response = self.pzn_seven_controller.get_data()
        return response, 200
