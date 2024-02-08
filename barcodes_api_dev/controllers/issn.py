from typing import Dict
from models.drivers import IssnHandler, ResponseFormatHandler
from models import IssnModel
from flask import jsonify


class IssnController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_issn_tag(product_code)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_issn_tag(self, product_code: str) -> str:
        issn_handler = IssnHandler()
        tag_name = issn_handler.create_issn_barcode(product_code)
        return tag_name

    def get_data(self) -> Dict:
        issn_model = IssnModel()
        return jsonify(issn_model.data)
