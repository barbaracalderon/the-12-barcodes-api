from typing import Dict
from flask import send_file
from dotenv import load_dotenv
import os


class ResponseFormatHandler:

    def format_response(self, tag_name: str) -> Dict:
        load_dotenv()
        tag_path = os.getenv("TAG_PATH")
        file_path = f"{tag_path}/{tag_name}.png"
        return send_file(file_path, as_attachment=True)
