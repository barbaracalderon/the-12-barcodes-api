from typing import Dict
from models.drivers import JanHandler, ResponseHandler
from models import JanModel
from flask import jsonify


class JanController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_jan_tag(product_number)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_jan_tag(self, product_number: str) -> str:
        jan_handler = JanHandler()
        barcode_tag = jan_handler.create_jan_barcode(product_number)
        return barcode_tag

    def get_data(self) -> Dict:
        jan_model = JanModel()
        return jsonify(jan_model.data)
