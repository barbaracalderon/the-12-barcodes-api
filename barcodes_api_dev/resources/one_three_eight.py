from flask_smorest import Blueprint
from flask.views import MethodView
from controllers import OneThreeEightController
from schemas import OneThreeEightSchema

blp = Blueprint("Barcode 138", __name__, description="Turn strings into a 138 barcode. Accepts alphanumeric characters.")


@blp.route("/one_three_eight")
class Barcode(MethodView):
    @blp.arguments(OneThreeEightSchema)
    def post(self, barcode_data):
        one_three_eight_controller = OneThreeEightController()
        response = one_three_eight_controller.create(barcode_data.get("product_name"))
        return response, 201
