#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema
from smelt_py.parsing import TypeMap
from smelt_py.parsing.converters import BuiltInConverter


def schema_to_type_map(schema: Schema):
    return TypeMap(**{
        type_key: BuiltInConverter(polars_type.to_python()) for
        type_key, polars_type in
        filter(lambda x: x[0] != "context_id", schema.items())
    })
