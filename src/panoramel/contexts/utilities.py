#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema
from smelt_py.parsing import Converter, TypeMap


def schema_to_type_map(schema: Schema):
    return TypeMap(**{
        type_key: Converter.for_built_in(polars_type.to_python()) for
        type_key, polars_type in
        filter(lambda x: x[0] != "context_id", schema.items())
    })
