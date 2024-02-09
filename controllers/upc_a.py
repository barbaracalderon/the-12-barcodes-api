from typing import Dict
from models.drivers import UpcAHandler, BufferedImageHandler, ResponseFormatHandler
from models import UpcAModel
from flask import jsonify


class UpcAController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_upc_a_tag(product_number)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_upc_a_tag(self, product_number: str) -> str:
        upc_handler = UpcAHandler()
        tag_name = upc_handler.create_upc_barcode(product_number)
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
        upc_a_model = UpcAModel()
        return jsonify(upc_a_model.data)
