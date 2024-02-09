from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import IssnController
from schemas import IssnSchema

blp = Blueprint(
    "Barcode ISSN",
    __name__,
    description="Operations on barcode ISSN.",
)


@blp.route("/issn")
class Barcode(MethodView):

    def __init__(self):
        self.issn_controller = IssnController()

    @blp.arguments(IssnSchema)
    def post(self, barcode_data):
        response = self.issn_controller.create(barcode_data.get("product_code"))
        return response, 201

    def get(self):
        response = self.issn_controller.get_data()
        return response, 200
