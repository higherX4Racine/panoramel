#  Copyright (C) 2025 by Higher Expectations for Racine County
from polars import Schema, String, Binary
from smelt_py.matching import (Element, Pattern)
from smelt_py.database.models.contexts import LookupContext

from .utilities import schema_to_type_map


class Ela(LookupContext):
    r"""A context that describes either a raw score or a success level.

        Parameters
        ----------
        unit: str
            either "Status" or "Value" for an achievement level or raw score.
        """
    _field_names = ["unit"]
    _name_field = "unit"
    _mapping = {
        "Status": String,
        "Value": String
    }
    def __init__(self, unit: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._unit = unit

    @property
    def unit(self) -> str:
        return self._unit

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
