from barcode.codex import Code128
from barcode.writer import ImageWriter


class OneTwoEightHandler:
    def create_one_two_eight_barcode(self, product_name: str) -> str:
        tag = Code128(code=product_name, writer=ImageWriter())
        tag_name = "barcode_128"
        tag.save(tag_name)
        return tag_name
