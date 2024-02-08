from barcode.isxn import InternationalStandardSerialNumber
from barcode.writer import ImageWriter


class IssnHandler:
    def create_issn_barcode(self, product_code: str) -> str:
        tag = InternationalStandardSerialNumber(product_code, writer=ImageWriter())
        tag_name = "barcode_issn"
        tag.save(tag_name)
        return tag_name
