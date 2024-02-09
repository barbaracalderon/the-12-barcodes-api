from typing import Dict
from models.drivers import PznSevenHandler, ResponseHandler
from models import PznSevenModel
from flask import jsonify


class PznSevenController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_pzn_seven_tag(product_number)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_pzn_seven_tag(self, product_number: str) -> str:
        pzn_seven_handler = PznSevenHandler()
        tag_name = pzn_seven_handler.create_pzn_seven_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        pzn_seven_model = PznSevenModel()
        return jsonify(pzn_seven_model.data)
