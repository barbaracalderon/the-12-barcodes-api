from typing import Dict
from models.drivers import EanOneFourHandler, ResponseHandler
from models import EanOneFourModel
from flask import jsonify


class EanOneFourController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_ean_one_four_tag(product_number)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_ean_one_four_tag(self, product_number: str) -> str:
        ean_one_four_handler = EanOneFourHandler()
        barcode_tag = ean_one_four_handler.create_ean_one_four_barcode(product_number)
        return barcode_tag

    def get_data(self) -> Dict:
        ean_one_four_model = EanOneFourModel()
        return jsonify(ean_one_four_model.data)
