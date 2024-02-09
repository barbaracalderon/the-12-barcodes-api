from barcode.upc import UniversalProductCodeA
from barcode.writer import ImageWriter


class UpcAHandler:
    def create_upc_barcode(self, product_number: str) -> str:
        try:
            tag = UniversalProductCodeA(upc=product_number, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
