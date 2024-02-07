from typing import Dict
from drivers.one_three_eight_handler import OneThreeEightHandler
from flask import send_file
import os
from dotenv import load_dotenv


class OneThreeEightController:

    def create(self, product_name: str) -> Dict:
        tag_path = self.__create_one_three_eight_tag(product_name)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_one_three_eight_tag(self, product_name: str) -> str:
        one_three_eight_handler = OneThreeEightHandler()
        tag_name = one_three_eight_handler.create_one_three_eight_barcode(product_name)
        return tag_name

    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)
