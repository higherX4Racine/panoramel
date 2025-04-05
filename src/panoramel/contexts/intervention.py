#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, Int8, String, Binary, Datetime

from smelt_py.models import LookupContext
from smelt_py.parsing import (Element, Parser, Pattern)

from panoramel.contexts.utilities import schema_to_type_map


@dataclass
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
    _name_field = "detail"
    _mapping = {
        "Status": String,
        "Start Date": String,
        "Type and Strategy": String,
        "Tier": String
    }
    number: int = None
    detail: str = None


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

PARSER = Parser(TYPE_MAP, PATTERN)
