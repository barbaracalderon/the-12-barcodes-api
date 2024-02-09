from typing import Dict
from models.drivers import EanOneThreeHandler, BufferedImageHandler, ResponseFormatHandler
from models import EanOneThreeModel
from flask import jsonify


class EanOneThreeController:

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_ean_one_three_tag(product_number)
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response = self.__create_formatted_response(buffered_image)
        return formatted_response

    def __create_ean_one_three_tag(self, product_number: str) -> str:
        ean_one_three_handler = EanOneThreeHandler()
        tag_name = ean_one_three_handler.create_ean_one_three_barcode(product_number)
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
        ean_one_three_model = EanOneThreeModel()
        return jsonify(ean_one_three_model.data)