from typing import Dict
from flask import send_file
from flask import jsonify
from models.drivers.buffered_image_handler import BufferedImageHandler


class ResponseHandler:

    def create_response(self, barcode_tag):
        if isinstance(barcode_tag, str):
            error_message = barcode_tag
            error_formatted_response, status_code = self.__format_error_response(
                error_message
            )
            return error_formatted_response, status_code

        buffered_image = self.__create_buffer_image(barcode_tag)
        formatted_response, status_code = self.__format_response(buffered_image)
        return formatted_response, status_code

    def __create_buffer_image(self, barcode_tag):
        buffered_image_handler = BufferedImageHandler()
        buffered_image = buffered_image_handler.create_buffer_image(barcode_tag)
        return buffered_image

    def __format_response(self, image_content) -> Dict:
        return (
            send_file(
                image_content,
                mimetype="image/png",
                as_attachment=True,
                download_name="barcode",
            ),
            201,
        )

    def __format_error_response(self, error_message: str) -> Dict:
        response = jsonify({"message": error_message})
        return response, 400
