from typing import Dict
from drivers import IssnHandler, ResponseFormatHandler


class IssnController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_issn_tag(product_code)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_issn_tag(self, product_code: str) -> str:
        issn_handler = IssnHandler()
        tag_name = issn_handler.create_issn_barcode(product_code)
        return tag_name
