#  Copyright (C) 2025 by Higher Expectations for Racine County
from dataclasses import dataclass
from polars import Schema, String, Binary
from smelt_py.parsing import (Element, Parser, Pattern)
from smelt_py.models import LookupContext

from .utilities import schema_to_type_map


@dataclass
class Ela(LookupContext):
    r"""A context that describes either a raw score or a success level.

    Parameters
    ----------
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    """
    _name_field = "unit"
    _mapping = {
        "Status": String,
        "Value": String
    }
    unit: str = None


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

PARSER = Parser(TYPE_MAP, PATTERN)
