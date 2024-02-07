from typing import Dict
from drivers import EanEightHandler
from flask import send_file
import os
from dotenv import load_dotenv


class EanEightController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_ean_eight_tag(product_number)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_ean_eight_tag(self, product_number: str) -> str:
        ean_eight_handler = EanEightHandler()
        tag_name = ean_eight_handler.create_ean_eight_barcode(product_number)
        return tag_name

    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)
