from typing import Dict
from models.drivers import EanOneThreeHandler, ResponseHandler
from models import EanOneThreeModel
from flask import jsonify


class EanOneThreeController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_ean_one_three_tag(product_number)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_ean_one_three_tag(self, product_number: str) -> str:
        ean_one_three_handler = EanOneThreeHandler()
        tag_name = ean_one_three_handler.create_ean_one_three_barcode(product_number)
        return tag_name

    def get_data(self) -> Dict:
        ean_one_three_model = EanOneThreeModel()
        return jsonify(ean_one_three_model.data)
