from typing import Dict
from models.drivers import PznSevenHandler, ResponseFormatHandler
from models import PznSevenModel
from flask import jsonify


class PznSevenController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_pzn_seven_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_pzn_seven_tag(self, product_number: str) -> str:
        pzn_seven_handler = PznSevenHandler()
        tag_name = pzn_seven_handler.create_pzn_seven_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        pzn_seven_model = PznSevenModel()
        return jsonify(pzn_seven_model.data)