from marshmallow import Schema, fields

class BarcodeSchema(Schema):
    product_name = fields.Str(required=True)