from typing import Dict
from drivers import IsbnOneThreeHandler, ResponseFormatHandler


class IsbnOneThreeController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_isbn_one_three_tag(product_code)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response

    def __create_isbn_one_three_tag(self, product_code: str) -> str:
        isbn_one_three_handler = IsbnOneThreeHandler()
        tag_name = isbn_one_three_handler.create_isbn_one_three_barcode(product_code)
        return tag_name
