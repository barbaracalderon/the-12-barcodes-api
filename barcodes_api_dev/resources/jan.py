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
    @blp.arguments(JanSchema)
    def post(self, barcode_data):
        jan_controller = JanController()
        response = jan_controller.create(barcode_data.get("product_number"))
        return response, 201
