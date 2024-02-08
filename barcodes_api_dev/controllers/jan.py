from typing import Dict
from models.drivers import JanHandler, ResponseFormatHandler



class JanController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_jan_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_jan_tag(self, product_number: str) -> str:
        jan_handler = JanHandler()
        tag_name = jan_handler.create_jan_barcode(product_number)
        return tag_name

