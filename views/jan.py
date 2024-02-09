from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import JanController
from schemas import JanSchema

blp = Blueprint(
    "Barcode JAN",
    __name__,
    description="Operations on barcode JAN.",
)


@blp.route("/jan")
class Barcode(MethodView):

    def __init__(self):
        self.jan_controller = JanController()

    @blp.arguments(JanSchema)
    def post(self, barcode_data):
        response, status_code = self.jan_controller.create(barcode_data.get("product_number"))
        return response, status_code

    def get(self):
        response = self.jan_controller.get_data()
        return response, 200
