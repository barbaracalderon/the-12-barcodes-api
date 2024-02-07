from typing import Dict
from drivers.barcode_handler import BarcodeHandler
from flask import send_file
import base64
import os
from dotenv import load_dotenv


class BarcodeController:

    def create(self, product_name: str) -> Dict:
        tag_path = self.__create_barcode_tag(product_name)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_barcode_tag(self, product_name: str) -> str:
        barcode_handler = BarcodeHandler()
        tag_name = barcode_handler.create_barcode(product_name)
        return tag_name

    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)
