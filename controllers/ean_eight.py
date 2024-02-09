from typing import Dict
from models.drivers import EanEightHandler, ResponseHandler
from models import EanEightModel
from flask import jsonify


class EanEightController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_ean_eight_tag(product_number)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_ean_eight_tag(self, product_number: str) -> str:
        ean_eight_handler = EanEightHandler()
        barcode_tag = ean_eight_handler.create_ean_eight_barcode(product_number)
        return barcode_tag

    def get_data(self) -> Dict:
        ean_eight_model = EanEightModel()
        return jsonify(ean_eight_model.data)
