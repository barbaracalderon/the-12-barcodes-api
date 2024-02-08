class UpcAModel:

    def __init__(self):
        self.data = {
            "name": "Universal Product Code-A (UPC-A)",
            "previous_name": [""],
            "type": "upc-a",
            "place_of_origin": "United States",
            "year": "1974",
            "density": "high",
            "usage_field": ["retail", "inventory management", "stores"],
            "maximum_characters": 12,
            "minimum_characters": 12,
            "accept_numbers": True,
            "accept_alphabet": False,
            "accept_special_characters": False,
            "encoding_scheme": ["ASCII"],
            "url_reference": "https://en.wikipedia.org/wiki/Universal_Product_Code",
            "others": "UPC-A (Universal Product Code-A) is a barcode symbology widely used in retail and inventory management systems. It consists of 12 numeric digits and is commonly found on consumer products for tracking and identification purposes, specially trade items in stores. UPC-A barcodes encode only numeric digits, representing the manufacturer and product information. These barcodes are essential for efficient point-of-sale operations, supply chain management, and product tracking.",
        }
