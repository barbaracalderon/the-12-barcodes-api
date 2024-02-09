from barcode.codex import Gs1_128
from barcode.writer import ImageWriter


class GsOneOneTwoEightHandler:

    def create_gs_one_one_two_eight_barcode(self, product_code: str) -> str:
        try:
            tag = Gs1_128(code=product_code, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
