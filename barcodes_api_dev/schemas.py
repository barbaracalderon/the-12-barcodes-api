from marshmallow import Schema, fields


class OneThreeEightSchema(Schema):
    product_name = fields.Str(required=True)


class UpcASchema(Schema):
    product_number = fields.Str(required=True)


class ThreeNineSchema(Schema):
    product_name = fields.Str(required=True)


class IssnSchema(Schema):
    product_code = fields.Str(required=True)


class IsbnTenSchema(Schema):
    product_code = fields.Str(required=True)


class IsbnOneThreeSchema(Schema):
    product_code = fields.Str(required=True)


class PznSevenSchema(Schema):
    product_number = fields.Str(required=True)


class EanOneThreeSchema(Schema):
    product_number = fields.Str(required=True)


class EanEightSchema(Schema):
    product_number = fields.Str(required=True)


class JanSchema(Schema):
    product_number = fields.Str(required=True)


class EanOneFourSchema(Schema):
    product_number = fields.Str(required=True)


class GsOneOneTwoEightSchema(Schema):
    product_code = fields.Str(required=True)
