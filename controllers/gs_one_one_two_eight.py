from typing import Dict
from models.drivers import (
    GsOneOneTwoEightHandler,
    BufferedImageHandler,
    ResponseFormatHandler,
)
from models import GsOneOneTwoEightModel
from flask import jsonify


class GsOneOneTwoEightController:

    def create(self, product_code: str) -> Dict:
        barcode_tag = self.__create_gs_one_one_two_eight_tag(product_code)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_gs_one_one_two_eight_tag(self, product_code: str) -> str:
        gs_one_one_two_eight_handler = GsOneOneTwoEightHandler()
        tag_name = gs_one_one_two_eight_handler.create_gs_one_one_two_eight_barcode(
            product_code
        )
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
        gs_one_one_two_eight_model = GsOneOneTwoEightModel()
        return jsonify(gs_one_one_two_eight_model.data)
