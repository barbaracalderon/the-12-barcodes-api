from barcode.ean import EAN14
from barcode.writer import ImageWriter


class EanOneFourHandler:

    def create_ean_one_four_barcode(self, product_number: str) -> str:
        tag = EAN14(ean=product_number, writer=ImageWriter())
        tag_name = "barcode_ean_14"
        tag.save(tag_name)
        return tag_name
