class IssnModel:

    def __init__(self):
        self.data = {
            "name": "International Standard Serial Number (ISSN)",
            "previous_name": ["ISO 3297"],
            "type": "issn",
            "place_of_origin": "International Collaboration",
            "year": "1975",
            "density": "high",
            "usage_field": ["publishing", "serial publications", "library management"],
            "maximum_characters": 8,
            "minimum_characters": 8,
            "accept_numbers": True,
            "accept_alphabet": True,
            "accept_special_characters": False,
            "encoding_scheme": ["ASCII"],
            "url_reference": "https://en.wikipedia.org/wiki/International_Standard_Serial_Number",
            "others": "ISSN (International Standard Serial Number) is a unique identifier for serial publications such as journals, magazines, and newspapers. It consists of 8 characters and was established to facilitate the identification and management of serial publications. When a serial with the same content is published in more than one media type, a different ISSN is assigned to each media type. ISSN barcodes encode both numeric digits and alphabet characters, allowing for a wide range of publication titles to be represented. These barcodes are used in the publishing industry and libraries for cataloging, subscription management, and inventory control purposes.",
        }
