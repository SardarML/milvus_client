from pymilvus import CollectionSchema, DataType, FieldSchema


def schema(dimension):
    fields = [
        FieldSchema("id", DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema("embedding", DataType.FLOAT_VECTOR, dim=dimension),
    ]
    return CollectionSchema(fields, enable_dynamic_field=True)