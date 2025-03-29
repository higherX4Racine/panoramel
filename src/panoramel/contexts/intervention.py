#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema, Int8, String, Binary, Datetime

from smelt_py.database.models.contexts import LookupContext
from smelt_py.matching import (Element, Pattern)

from panoramel.contexts.utilities import schema_to_type_map


class Intervention(LookupContext):
    r"""Details about a learning intervention to help a kid get up to standard.

    Parameters
    ----------
    number: int
        Interventions are identified by increasing sequential values
    detail: str
        One of several possible values

        One of intervention status <str>, start date <date>, type <str>, or
        tier <str>.
    """
    _field_names = ["number", "detail"]
    _name_field = "detail"
    _mapping = {
        "Status": String,
        "Start Date": String,
        "Type and Strategy": String,
        "Tier": String
    }

    def __init__(self, number: int, detail: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._number = number
        self._detail = detail

    @property
    def number(self) -> int:
        return self._number

    @property
    def detail(self) -> str:
        return self._detail


PATTERN = Pattern(
    [
        Element(pattern=r"Intervention"),
        Element(name="number", pattern=r"\d+"),
        Element(name="detail", pattern=r".+")
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    number=Int8,
    detail=String
))

TYPE_MAP = schema_to_type_map(SCHEMA)
