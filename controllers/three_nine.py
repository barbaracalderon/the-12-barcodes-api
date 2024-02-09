from typing import Dict
from models.drivers import ThreeNineHandler, ResponseHandler
from models import ThreeNineModel
from flask import jsonify


class ThreeNineController:

    def create(self, product_name: str) -> Dict:
        barcode_tag = self.__create_three_nine_tag(product_name)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_three_nine_tag(self, product_name: str) -> str:
        three_nine_handler = ThreeNineHandler()
        tag_name = three_nine_handler.create_three_nine_barcode(product_name)
        return tag_name

    def get_data(self) -> Dict:
        three_nine_model = ThreeNineModel()
        return jsonify(three_nine_model.data)
