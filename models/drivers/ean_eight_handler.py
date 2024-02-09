from barcode.ean import EAN8
from barcode.writer import ImageWriter


class EanEightHandler:

    def create_ean_eight_barcode(self, product_number: str) -> str:
        tag = EAN8(ean=product_number, writer=ImageWriter())
        return tag
