from typing import Dict
from models.drivers import ThreeNineHandler, ResponseFormatHandler
from models import ThreeNineModel
from flask import jsonify


class ThreeNineController:

    def create(self, product_name: str) -> Dict:
        tag_path = self.__create_three_nine_tag(product_name)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_three_nine_tag(self, product_name: str) -> str:
        three_nine_handler = ThreeNineHandler()
        tag_name = three_nine_handler.create_three_nine_barcode(product_name)
        return tag_name

    def get_data(self) -> Dict:
        three_nine_model = ThreeNineModel()
        return jsonify(three_nine_model.data)