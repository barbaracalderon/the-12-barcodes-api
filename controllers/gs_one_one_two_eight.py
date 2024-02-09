from typing import Dict
from models.drivers import (
    GsOneOneTwoEightHandler,
    ResponseHandler,
)
from models import GsOneOneTwoEightModel
from flask import jsonify


class GsOneOneTwoEightController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_gs_one_one_two_eight_tag(product_code)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_gs_one_one_two_eight_tag(self, product_code: str) -> str:
        gs_one_one_two_eight_handler = GsOneOneTwoEightHandler()
        tag_name = gs_one_one_two_eight_handler.create_gs_one_one_two_eight_barcode(
            product_code
        )
        return tag_name

    def get_data(self) -> Dict:
        gs_one_one_two_eight_model = GsOneOneTwoEightModel()
        return jsonify(gs_one_one_two_eight_model.data)
