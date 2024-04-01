from marshmallow import Schema, fields


class TagSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class PetsSchema(Schema):
    id = fields.Int(required=True)
    category = fields.Nested(CategorySchema, required=True)
    name = fields.Str(required=True)
    photoUrls = fields.List(fields.String(), required=True)
    tags = fields.List(fields.Nested(TagSchema), required=True)
    status = fields.Str(required=True)

