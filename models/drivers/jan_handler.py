from barcode.ean import JapanArticleNumber
from barcode.writer import ImageWriter


class JanHandler:
    def create_jan_barcode(self, product_number: str) -> str:
        tag = JapanArticleNumber(jan=product_number, writer=ImageWriter())
        return tag
