from barcode.isxn import InternationalStandardBookNumber10
from barcode.writer import ImageWriter


class IsbnTenHandler:

    def create_isbn_ten_barcode(self, product_code: str) -> str:
        try:
            tag = InternationalStandardBookNumber10(
                isbn=product_code, writer=ImageWriter()
            )
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
