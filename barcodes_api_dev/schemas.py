from marshmallow import Schema, fields


class OneThreeEightSchema(Schema):
    product_name = fields.Str(required=True)


class UpcSchema(Schema):
    product_number = fields.Str(required=True)
