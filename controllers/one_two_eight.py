from typing import Dict
from models.drivers import (
    OneTwoEightHandler,
    ResponseHandler,
)
from models import OneTwoEightModel
from flask import jsonify


class OneTwoEightController:

    def create(self, product_name: str) -> Dict:
        barcode_tag = self.__create_one_two_eight_tag(product_name)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_one_two_eight_tag(self, product_name: str) -> str:
        one_two_eight_handler = OneTwoEightHandler()
        tag_name = one_two_eight_handler.create_one_two_eight_barcode(product_name)
        return tag_name

    def get_data(self) -> Dict:
        one_two_eight_model = OneTwoEightModel()
        return jsonify(one_two_eight_model.data)
