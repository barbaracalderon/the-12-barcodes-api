from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request
from controllers.barcode import BarcodeController
from schemas import BarcodeSchema


blp = Blueprint("barcode", __name__, description="Turn strings into barcodes.")


@blp.route("/barcode")
class Barcode(MethodView):
    @blp.arguments(BarcodeSchema)
    def post(self, barcode_data):
        barcode_controller = BarcodeController()
        response = barcode_controller.create(barcode_data.get("product_name"))
        return response, 201
