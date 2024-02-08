class EanEightModel:

    def __init__(self):
        self.data = {
            "name": "European Article Number 8 (EAN-8)",
            "previous_name": "",
            "type": "ean-8",
            "place_of_origin": "Europe",
            "year": "1977",
            "density": "low",
            "usage_field": ["retail", "consumer goods", "inventory management"],
            "maximum_characters": 8,
            "minimum_characters": 8,
            "accept_numbers": True,
            "accept_alphabet": False,
            "accept_special_characters": False,
            "encoding_scheme": ["ASCII"],
            "url_reference": "https://en.wikipedia.org/wiki/EAN-8",
            "others": "EAN-8 (European Article Number) is a barcode symbology used worldwide for retail and consumer goods. It consists of 8 digits and is used to uniquely identify products in stores, especially when space is limited. EAN-8 barcodes encode only numeric digits and do not include alphabet characters or special characters. They are commonly used for smaller items, such as individual pieces of fruit or small consumer goods.",
        }
