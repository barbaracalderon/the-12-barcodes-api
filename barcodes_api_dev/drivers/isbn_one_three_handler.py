from barcode.isxn import InternationalStandardBookNumber13
from barcode.writer import ImageWriter


class IsbnOneThreeHandler:

    def create_isbn_one_three_barcode(self, product_code: str) -> str:
        tag = InternationalStandardBookNumber13(isbn=product_code, writer=ImageWriter())
        tag_name = "barcode_isbn_13"
        tag.save(tag_name)
        return tag_name