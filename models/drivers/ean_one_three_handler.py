from barcode.ean import EAN13
from barcode.writer import ImageWriter


class EanOneThreeHandler:

    def create_ean_one_three_barcode(self, product_number: str) -> str:
        tag = EAN13(ean=product_number, writer=ImageWriter())
        return tag
