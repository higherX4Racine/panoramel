#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from polars import Schema, String, Binary, Float64
from smelt_py.models import LookupContext
from smelt_py.parsing import (Element, Parser, Pattern)
from .utilities import schema_to_type_map


@dataclass
class Forward(LookupContext):
    r"""One specific early literacy assessment

    Parameters
    ----------
    subject: str
        The subject assessed by this part of the Forward exam
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    """
    _name_field = "unit"
    _mapping = {
        "Most Recent Result": Float64,
        "Status": String,
        "Value": Float64
    }
    subject: str = None
    unit: str = None


PATTERN = Pattern(
    [
        Element(pattern=r"Forward"),
        Element(pattern=r"-"),
        Element(name="subject", pattern=r"ELA|Math\\w*"),
        Element(name="unit", pattern=r"Most Recent Result|Status")
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    subject=String,
    unit=String,
))

TYPE_MAP = schema_to_type_map(SCHEMA)

PARSER = Parser(TYPE_MAP, PATTERN)
