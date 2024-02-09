from typing import Dict
from models.drivers import PznSevenHandler, BufferedImageHandler, ResponseFormatHandler
from models import PznSevenModel
from flask import jsonify


class PznSevenController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_pzn_seven_tag(product_number)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_pzn_seven_tag(self, product_number: str) -> str:
        pzn_seven_handler = PznSevenHandler()
        tag_name = pzn_seven_handler.create_pzn_seven_barcode(product_number)
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
        pzn_seven_model = PznSevenModel()
        return jsonify(pzn_seven_model.data)
