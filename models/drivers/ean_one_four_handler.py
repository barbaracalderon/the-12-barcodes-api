from barcode.ean import EAN14
from barcode.writer import ImageWriter


class EanOneFourHandler:

    def create_ean_one_four_barcode(self, product_number: str) -> str:
        try:
            tag = EAN14(ean=product_number, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
