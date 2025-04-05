#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String, Int16, Binary, Boolean, Float64

from smelt_py.models import LookupContext
from smelt_py.parsing import (Element, Parser, Pattern, TypeMap)
from smelt_py.parsing.converters import Converter, BuiltInConverter


@dataclass
class NweaMap(LookupContext):
    r"""A complicated heading with information about a MAP score.
    Parameters
    ----------
    score_type: str
        whether it is raw or growth or something else
    subject: str
        math or language. abbreviations vary
    grade_range: str
        something 4K-12
    edition: str
        further detail, e.g. English or Spanish or SPED
    year: int
        4-digit year when the test was taken
    version: str
        even more specific detail than `edition`
    season: str
        fall, winter, or spring
    duplicated: bool
        some of the columns mark the MAP score as repeated.
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    """

    _name_field = "unit"
    _mapping = {
        "Most Recent Result": Float64,
        "Status": String,
        "Value": Float64
    }

    score_type: str = None
    subject: str = None
    grade_range: str = None
    edition: str = None
    year: int = None
    version: str = None
    season: str = None
    duplicated: bool = False
    unit: str = ""


PATTERN = Pattern(
    [
        Element(pattern=r"NWEA MAP"),
        Element(name="score_type", pattern=r"Growth"),
        Element(name="subject", pattern=r"Math\w*|(Spanish )?Reading"),
        Element(name="grade_range", pattern=r"\S+"),
        Element(name="edition", pattern=r"\S+"),
        Element(name="year", pattern=r"\b\d+\b"),
        Element(name="version", pattern=r"V\d", required=False),
        Element(name="season", pattern=r"Fall|Winter|Spring"),
        Element(name="unit", pattern=r"Status|Value"),
        Element(name="duplicated", pattern=r"_duplicated_\d+", required=False)
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    score_type=String,
    subject=String,
    grade_range=String,
    edition=String,
    year=Int16,
    version=String,
    season=String,
    duplicated=Boolean,
    unit=String,
))

TYPE_MAP = TypeMap(
    score_type=BuiltInConverter(str),
    subject=BuiltInConverter(str),
    grade_range=BuiltInConverter(str),
    edition=BuiltInConverter(str),
    year=BuiltInConverter(int),
    version=BuiltInConverter(str),
    season=BuiltInConverter(str),
    duplicated=BuiltInConverter(bool),
    unit=BuiltInConverter(str),
)

PARSER = Parser(TYPE_MAP, PATTERN)
