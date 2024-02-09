from typing import Dict
from models.drivers import EanOneFourHandler, ResponseFormatHandler
from models import EanOneFourModel
from flask import jsonify


class EanOneFourController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_ean_one_four_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_ean_one_four_tag(self, product_number: str) -> str:
        ean_one_four_handler = EanOneFourHandler()
        tag_name = ean_one_four_handler.create_ean_one_four_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        ean_one_four_model = EanOneFourModel()
        return jsonify(ean_one_four_model.data)