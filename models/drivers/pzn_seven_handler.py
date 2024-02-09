from barcode.codex import PZN7
from barcode.writer import ImageWriter


class PznSevenHandler:

    def create_pzn_seven_barcode(self, product_number: str) -> str:
        tag = PZN7(pzn=product_number, writer=ImageWriter())
        return tag
