from typing import Dict
from drivers import JanHandler
from flask import send_file
import os
from dotenv import load_dotenv


class JanController:

    def create(self, product_number: str) -> Dict:
        tag_path = self.__create_jan_tag(product_number)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_jan_tag(self, product_number: str) -> str:
        jan_handler = JanHandler()
        tag_name = jan_handler.create_jan_barcode(product_number)
        return tag_name

    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)