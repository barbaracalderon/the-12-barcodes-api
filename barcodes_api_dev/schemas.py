from marshmallow import Schema, fields

class OneThreeEightSchema(Schema):
    product_name = fields.Str(required=True)