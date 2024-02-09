from barcode.codex import Code128
from barcode.writer import ImageWriter


class OneTwoEightHandler:
    def create_one_two_eight_barcode(self, product_name: str) -> str:
        try:
            tag = Code128(code=product_name, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
