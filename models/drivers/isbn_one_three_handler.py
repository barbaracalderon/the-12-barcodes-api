from barcode.isxn import InternationalStandardBookNumber13
from barcode.writer import ImageWriter


class IsbnOneThreeHandler:

    def create_isbn_one_three_barcode(self, product_code: str) -> str:
        try:
            tag = InternationalStandardBookNumber13(
                isbn=product_code, writer=ImageWriter()
            )
            return tag
        except Exception as e:
            error_message = str(e)
            return error_message
