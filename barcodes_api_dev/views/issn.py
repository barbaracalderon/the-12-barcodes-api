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
    @blp.arguments(IssnSchema)
    def post(self, barcode_data):
        issn_controller = IssnController()
        response = issn_controller.create(barcode_data.get("product_code"))
        return response, 201