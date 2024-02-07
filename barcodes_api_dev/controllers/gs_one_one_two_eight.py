from typing import Dict
from drivers import GsOneOneTwoEightHandler, ResponseFormatHandler


class GsOneOneTwoEightController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_gs_one_one_two_eight_tag(product_code)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_gs_one_one_two_eight_tag(self, product_code: str) -> str:
        gs_one_one_two_eight_handler = GsOneOneTwoEightHandler()
        tag_name = gs_one_one_two_eight_handler.create_gs_one_one_two_eight_barcode(
            product_code
        )
        return tag_name

