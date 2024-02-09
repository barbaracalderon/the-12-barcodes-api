from typing import Dict
from models.drivers import UpcAHandler, ResponseFormatHandler
from models import UpcAModel
from flask import jsonify


class UpcAController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_upc_a_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_upc_a_tag(self, product_number: str) -> str:
        upc_handler = UpcAHandler()
        tag_name = upc_handler.create_upc_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        upc_a_model = UpcAModel()
        return jsonify(upc_a_model.data)
