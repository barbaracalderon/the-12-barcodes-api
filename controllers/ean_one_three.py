from typing import Dict
from models.drivers import EanOneThreeHandler, ResponseFormatHandler
from models import EanOneThreeModel
from flask import jsonify


class EanOneThreeController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_ean_one_three_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_ean_one_three_tag(self, product_number: str) -> str:
        ean_one_three_handler = EanOneThreeHandler()
        tag_name = ean_one_three_handler.create_ean_one_three_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        ean_one_three_model = EanOneThreeModel()
        return jsonify(ean_one_three_model.data)