from barcode.isxn import InternationalStandardBookNumber10
from barcode.writer import ImageWriter

class IsbnTenHandler:

    def create_isbn_ten_barcode(self, product_code: str) -> str:
        tag = InternationalStandardBookNumber10(isbn=product_code, writer=ImageWriter())
        tag_name = "barcode_isbn_10"
        tag.save(tag_name)
        return tag_name