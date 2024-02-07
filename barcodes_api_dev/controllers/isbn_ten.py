from typing import Dict
from drivers import IsbnTenHandler, ResponseFormatHandler


class IsbnTenController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_isbn_ten_tag(product_code)
        response_format_handler = ResponseFormatHandler()
        formatted_response = response_format_handler.format_response(tag_path)
        return formatted_response
    
    def __create_isbn_ten_tag(self, product_code: str) -> str:
        isbn_ten_handler = IsbnTenHandler()
        tag_name = isbn_ten_handler.create_isbn_ten_barcode(product_code)
        return tag_name
    
