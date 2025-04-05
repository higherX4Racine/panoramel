#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import (
    Binary,
    Int8,
    Int16,
    Float64,
    Schema,
    String,
)

from smelt_py.models import LookupContext
from smelt_py.parsing import (
    Element,
    Parser,
    Pattern,
    TypeMap,
)
from smelt_py.parsing.converters import (
    BuiltInConverter,
    MonthConverter,
)


@dataclass
class ElAssessment(LookupContext):
    r"""One specific early literacy assessment

    Parameters
    ----------
    assessment: str
        The name of the assessment, like "Nonsense Words" or "ORF."
    month: str
        some sloppy representation of the month, like "01" or "Octo."
    year: int
        the four-digit calendar year that the assessment was done in.
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    """
    _name_field = "unit"
    _mapping = {
        "Most Recent Result": Float64,
        "Status": String,
        "Value": Float64
    }
    assessment: str = None
    month: str = None
    year: int = None
    unit: str = None


PATTERN = Pattern(
    [
        Element(name="assessment", pattern=r".+"),
        Element(name="month", pattern=r"\b\w+\b"),
        Element(name="year", pattern=r"\b\d+\b"),
        Element(name="unit", pattern=r"Status|Value")
    ],
    r"[\s:]"
)

TYPE_MAP = TypeMap(
    assessment=BuiltInConverter(str),
    month=MonthConverter("en"),
    year=BuiltInConverter(int),
    unit=BuiltInConverter(str),
)

PARSER = Parser(TYPE_MAP, PATTERN)

SCHEMA = Schema(dict(
    context_id=Binary,
    assessment=String,
    month=Int8,
    year=Int16,
    unit=String
))
