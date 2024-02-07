from typing import Dict
from drivers import IssnHandler
from flask import send_file
import os
from dotenv import load_dotenv


class IssnController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_issn_tag(product_code)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_issn_tag(self, product_code: str) -> str:
        issn_handler = IssnHandler()
        tag_name = issn_handler.create_issn_barcode(product_code)
        return tag_name

    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)
