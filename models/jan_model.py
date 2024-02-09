class JanModel:

    def __init__(self):
        self.data = {
            "name": "Japanese Article Number (JAN)",
            "previous_name": "",
            "type": "jan",
            "place_of_origin": "Japan",
            "year": "1978",
            "density": "high",
            "usage_field": ["retail", "consumer goods", "inventory management"],
            "maximum_characters": 13,
            "minimum_characters": 13,
            "accept_numbers": True,
            "accept_alphabet": False,
            "accept_special_characters": False,
            "encoding_scheme": ["ASCII", "ISO-8859-1"],
            "url_reference": "https://en.wikipedia.org/wiki/Japanese_Article_Number",
            "others": "JAN (Japanese Article Number) is a barcode symbology used primarily in Japan for retail and consumer goods. It is similar to the EAN-13 symbology but uses a different numbering system. JAN barcodes consist of 13 digits, where the first three digits of the JAN (Japanese Article Number) barcode, known as the GS1 Prefix, typically denote the GS1 Member Organization to which the manufacturer is affiliated. This does not necessarily indicate the country where the product is manufactured. Notably, GS1 reserves the 020-029 GS1 Prefix range for retailer internal use or internal use by other types of businesses.",
        }
