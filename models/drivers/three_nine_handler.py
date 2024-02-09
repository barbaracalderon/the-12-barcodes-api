from barcode.codex import Code39
from barcode.writer import ImageWriter


class ThreeNineHandler:
    def create_three_nine_barcode(self, product_name: str) -> str:
        try:
            tag = Code39(code=product_name, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
