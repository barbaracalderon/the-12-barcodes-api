from barcode.isxn import InternationalStandardSerialNumber
from barcode.writer import ImageWriter


class IssnHandler:
    def create_issn_barcode(self, product_code: str) -> str:
        try:
            tag = InternationalStandardSerialNumber(product_code, writer=ImageWriter())
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
