from typing import Dict
from models.drivers import UpcAHandler, ResponseHandler
from models import UpcAModel
from flask import jsonify


class UpcAController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_upc_a_tag(product_number)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_upc_a_tag(self, product_number: str) -> str:
        upc_handler = UpcAHandler()
        tag_name = upc_handler.create_upc_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        upc_a_model = UpcAModel()
        return jsonify(upc_a_model.data)
