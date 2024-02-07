from typing import Dict
from drivers import OneThreeEightHandler, ResponseFormatHandler


class OneThreeEightController:

    def create(self, product_name: str) -> Dict:
        tag_path = self.__create_one_three_eight_tag(product_name)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_one_three_eight_tag(self, product_name: str) -> str:
        one_three_eight_handler = OneThreeEightHandler()
        tag_name = one_three_eight_handler.create_one_three_eight_barcode(product_name)
        return tag_name
