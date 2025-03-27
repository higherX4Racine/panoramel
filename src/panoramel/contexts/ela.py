#  Copyright (C) 2025 by Higher Expectations for Racine County
from polars import Schema, String, Binary
from smelt_py.matching import (Element, Pattern)

from .status_value_unit_lookup import StatusValueUnit
from .utilities import schema_to_type_map


class Ela(StatusValueUnit):
    r"""English Language Arts context"""
    pass


PATTERN = Pattern(
    [
        Element(pattern=r"^ELA"),
        Element(name="unit", pattern=r"Status|Value", )
    ],
    r"[\s:]"
)

SCHEMA = Schema({
    "context_id": Binary,
    "unit": String
})

TYPE_MAP = schema_to_type_map(SCHEMA)
