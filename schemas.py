from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class StoreUpdateSchema(Schema):
    name = fields.Str()


class TagUpdateSchema(Schema):
    name = fields.Str()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    stores = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.Nested(PlainTagSchema(), many=True, dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.Nested(PlainItemSchema(), many=True, dump_only=True)
    tags = fields.Nested(PlainTagSchema(), many=True, dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(dump_only=True)
    stores = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.Nested(PlainItemSchema(), many=True, dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
