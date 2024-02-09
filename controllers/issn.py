from typing import Dict
from models.drivers import IssnHandler, ResponseHandler
from models import IssnModel
from flask import jsonify


class IssnController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_issn_tag(product_code)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_issn_tag(self, product_code: str) -> str:
        issn_handler = IssnHandler()
        tag_name = issn_handler.create_issn_barcode(product_code)
        return tag_name

    def get_data(self) -> Dict:
        issn_model = IssnModel()
        return jsonify(issn_model.data)
