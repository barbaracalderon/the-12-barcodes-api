from typing import Dict
from models.drivers import IsbnTenHandler, BufferedImageHandler, ResponseFormatHandler
from models import IsbnTenModel
from flask import jsonify


class IsbnTenController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_isbn_ten_tag(product_code)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_isbn_ten_tag(self, product_code: str) -> str:
        isbn_ten_handler = IsbnTenHandler()
        tag_name = isbn_ten_handler.create_isbn_ten_barcode(product_code)
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
        isbn_ten_model = IsbnTenModel()
        return jsonify(isbn_ten_model.data)
