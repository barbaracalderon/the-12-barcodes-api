from barcode.codex import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, product_name: str) -> str:
        tag = Code128(code=product_name, writer=ImageWriter())
        tag_name = "barcode"
        tag.save(tag_name)
        return tag_name
