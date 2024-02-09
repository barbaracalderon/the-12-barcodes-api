from typing import Dict
from models.drivers import (
    IsbnOneThreeHandler,
    BufferedImageHandler,
    ResponseFormatHandler,
)
from models import IsbnOneThreeModel
from flask import jsonify


class IsbnOneThreeController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_isbn_one_three_tag(product_code)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_isbn_one_three_tag(self, product_code: str) -> str:
        isbn_one_three_handler = IsbnOneThreeHandler()
        tag_name = isbn_one_three_handler.create_isbn_one_three_barcode(product_code)
        return tag_name

    def __create_buffer_image(self, barcode_tag):
        buffered_image_handler = BufferedImageHandler()
        buffered_image = buffered_image_handler.create_buffer_image(barcode_tag)
        return buffered_image

    def __create_formatted_response(self, buffered_image):
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(buffered_image)
        return formatted_response

    def get_data(self) -> Dict:
        isbn_one_three_model = IsbnOneThreeModel()
        return jsonify(isbn_one_three_model.data)
