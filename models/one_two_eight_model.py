class OneTwoEightModel:

    def __init__(self):
        self.data = {
            "name": "Code 128",
            "previous_name": "UCC/EAN-128",
            "type": "code-128",
            "place_of_origin": "United States",
            "year": "1977",
            "density": "compact",
            "usage_field": ["shipping", "package", "supply chain"],
            "maximum_characters": None,
            "minimum_characters": None,
            "accept_numbers": True,
            "accept_alphabet": True,
            "accept_special_characters": True,
            "encoding_scheme": ["ASCII", "ISO-8859-1"],
            "url_reference": "https://en.wikipedia.org/wiki/Code_128",
            "others": "Code 128 is a high-density barcode format, capable of encoding large amounts of data in a compact space. It is widely used in industries such as shipping, package tracking, and supply chain management due to its versatility and efficiency. Code 128 supports three different character sets: A, B, and C, allowing it to encode numeric data more efficiently using a double-density format. It is often used in conjunction with GS1 standards for barcode labeling in retail and logistics applications. Code 128 barcodes do not include human-readable characters by default, but they can be optionally added for easier manual interpretation.",
        }
