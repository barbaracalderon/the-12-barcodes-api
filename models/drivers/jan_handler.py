from barcode.ean import JapanArticleNumber
from barcode.writer import ImageWriter


class JanHandler:
    def create_jan_barcode(self, product_number: str) -> str:
        try:
            tag = JapanArticleNumber(jan=product_number, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
