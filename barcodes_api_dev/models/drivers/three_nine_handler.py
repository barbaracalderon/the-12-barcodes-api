from barcode.codex import Code39
from barcode.writer import ImageWriter


class ThreeNineHandler:
    def create_three_nine_barcode(self, product_name: str) -> str:
        tag = Code39(code=product_name, writer=ImageWriter())
        tag_name = "barcode_39"
        tag.save(tag_name)
        return tag_name