from typing import Dict
from models.drivers import JanHandler, BufferedImageHandler, ResponseFormatHandler
from models import JanModel
from flask import jsonify


class JanController:

    def __init__(self):
        self.response_format_handler = ResponseFormatHandler()

    def create(self, product_number: str) -> Dict:
        barcode_tag = self.__create_jan_tag(product_number)

        if isinstance(barcode_tag, str):
            error_message = barcode_tag
            error_formatted_response = self.__create_error_formatted_response(error_message)
            return error_formatted_response
        
        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response, status_code = self.__create_formatted_response(buffered_image)
        return formatted_response, status_code

    def __create_jan_tag(self, product_number: str) -> str:
        jan_handler = JanHandler()
        barcode_tag = jan_handler.create_jan_barcode(product_number)
        return barcode_tag

    def __create_buffer_image(self, barcode_tag):
        buffered_image_handler = BufferedImageHandler()
        buffered_image = buffered_image_handler.create_buffer_image(barcode_tag)
        return buffered_image

    def __create_formatted_response(self, buffered_image):
        formatted_response = self.response_format_handler.format_response(buffered_image)
        return formatted_response
    
    def __create_error_formatted_response(self, error_message: str) -> Dict:
        error_formatted_response, status_code = self.response_format_handler.format_error_response(error_message)
        return error_formatted_response, status_code

    def get_data(self) -> Dict:
        jan_model = JanModel()
        return jsonify(jan_model.data)
