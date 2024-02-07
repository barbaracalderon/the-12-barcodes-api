from typing import Dict
from drivers import PznSevenHandler, ResponseFormatHandler


class PznSevenController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_pzn_seven_tag(product_number)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_pzn_seven_tag(self, product_number: str) -> str:
        pzn_seven_handler = PznSevenHandler()
        tag_name = pzn_seven_handler.create_pzn_seven_barcode(product_number)
        return tag_name
