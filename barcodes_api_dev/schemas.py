from marshmallow import Schema, fields


class OneThreeEightSchema(Schema):
    product_name = fields.Str(required=True)


class UpcSchema(Schema):
    product_number = fields.Str(required=True)


class ThreeNineSchema(Schema):
    product_name = fields.Str(required=True)


class IssnSchema(Schema):
    product_code = fields.Str(required=True)


class IsbnTenSchema(Schema):
    product_code = fields.Str(required=True)
