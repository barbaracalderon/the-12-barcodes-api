from typing import Dict
from models.drivers import IsbnTenHandler, ResponseHandler
from models import IsbnTenModel
from flask import jsonify


class IsbnTenController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_isbn_ten_tag(product_code)
        response_handler = ResponseHandler()
        response, status_code = response_handler.create_response(barcode_tag)
        return response, status_code

    def __create_isbn_ten_tag(self, product_code: str) -> str:
        isbn_ten_handler = IsbnTenHandler()
        tag_name = isbn_ten_handler.create_isbn_ten_barcode(product_code)
        return tag_name

    def get_data(self) -> Dict:
        isbn_ten_model = IsbnTenModel()
        return jsonify(isbn_ten_model.data)
