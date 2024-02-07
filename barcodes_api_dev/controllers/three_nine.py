from typing import Dict
from drivers import ThreeNineHandler
from flask import send_file
import os
from dotenv import load_dotenv

class ThreeNineController:

    def create(self, product_name: str) -> Dict:
        tag_path = self.__create_three_nine_tag(product_name)
        formatted_response = self.__format_response(tag_path)
        return formatted_response
    
    def __create_three_nine_tag(self, product_name: str) -> str:
        three_nine_handler = ThreeNineHandler()
        tag_name = three_nine_handler.create_three_nine_barcode(product_name)
        return tag_name
    
    def __format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)