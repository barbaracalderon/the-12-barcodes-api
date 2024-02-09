from typing import Dict
from flask import send_file


class ResponseFormatHandler:

    def format_response(self, image_content) -> Dict:
        return send_file(
            image_content,
            mimetype="image/png",
            as_attachment=True,
            download_name="barcode",
        )
