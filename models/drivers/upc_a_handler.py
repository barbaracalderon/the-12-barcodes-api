from barcode.upc import UniversalProductCodeA
from barcode.writer import ImageWriter


class UpcAHandler:
    def create_upc_barcode(self, product_number: str) -> str:
        tag = UniversalProductCodeA(upc=product_number, writer=ImageWriter())
        tag_name = "barcode_upc_a"
        tag.save(tag_name)
        return tag_name
