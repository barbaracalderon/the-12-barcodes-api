from typing import Dict
from models.drivers import (
    IsbnOneThreeHandler,
    ResponseHandler,
)
from models import IsbnOneThreeModel
from flask import jsonify


class IsbnOneThreeController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_isbn_one_three_tag(product_code)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_isbn_one_three_tag(self, product_code: str) -> str:
        isbn_one_three_handler = IsbnOneThreeHandler()
        tag_name = isbn_one_three_handler.create_isbn_one_three_barcode(product_code)
        return tag_name

    def get_data(self) -> Dict:
        isbn_one_three_model = IsbnOneThreeModel()
        return jsonify(isbn_one_three_model.data)
