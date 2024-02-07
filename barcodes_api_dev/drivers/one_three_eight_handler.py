from barcode.codex import Code128
from barcode.writer import ImageWriter


class OneThreeEightHandler:
    def create_one_three_eight_barcode(self, product_name: str) -> str:
        tag = Code128(code=product_name, writer=ImageWriter())
        tag_name = "one_three_eight"
        tag.save(tag_name)
        return tag_name
