from typing import Dict
from models.drivers import (
    OneTwoEightHandler,
    BufferedImageHandler,
    ResponseFormatHandler,
)
from models import OneTwoEightModel
from flask import jsonify


class OneTwoEightController:

    def create(self, product_name: str) -> Dict:
        barcode_tag = self.__create_one_two_eight_tag(product_name)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_one_two_eight_tag(self, product_name: str) -> str:
        one_two_eight_handler = OneTwoEightHandler()
        tag_name = one_two_eight_handler.create_one_two_eight_barcode(product_name)
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
        one_two_eight_model = OneTwoEightModel()
        return jsonify(one_two_eight_model.data)
