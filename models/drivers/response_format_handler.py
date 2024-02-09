from typing import Dict
from flask import send_file
from flask import jsonify


class ResponseFormatHandler:

    def format_response(self, image_content) -> Dict:
        return send_file(
            image_content,
            mimetype="image/png",
            as_attachment=True,
            download_name="barcode",
        ), 201

    def format_error_response(self, error_message: str) -> Dict:
        response = jsonify({"message": error_message})
        return response, 400