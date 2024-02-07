from typing import Dict
from drivers import GsOneOneTwoEightHandler
from flask import send_file
import os
from dotenv import load_dotenv


class GsOneOneTwoEightController:

    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_gs_one_one_two_eight_tag(product_code)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_gs_one_one_two_eight_tag(self, product_code: str) -> str:
        gs_one_one_two_eight_handler = GsOneOneTwoEightHandler()
        tag_name = gs_one_one_two_eight_handler.create_gs_one_one_two_eight_barcode(
            product_code
        )
        return tag_name

    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)
