from typing import Dict
from drivers import UpcAHandler, ResponseFormatHandler


class UpcAController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_upc_a_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_upc_a_tag(self, product_number: str) -> str:
        upc_handler = UpcAHandler()
        tag_name = upc_handler.create_upc_barcode(product_number)
        return tag_name
