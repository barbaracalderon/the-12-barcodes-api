from typing import Dict
from models.drivers import EanEightHandler, ResponseFormatHandler


class EanEightController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_ean_eight_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_ean_eight_tag(self, product_number: str) -> str:
        ean_eight_handler = EanEightHandler()
        tag_name = ean_eight_handler.create_ean_eight_barcode(product_number)
        return tag_name
