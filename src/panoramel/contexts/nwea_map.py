#  Copyright (C) 2025 by Higher Expectations for Racine County
import polars
from polars import Schema, String, Int16, Binary, Boolean

from smelt_py.matching import (Element, Pattern)
from smelt_py.parsing import TypeMap, Converter

from .status_value_unit_lookup import StatusValueUnit


class NweaMap(StatusValueUnit):
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
    duplicated: str, optional
        some of the columns mark the MAP score as repeated.
    """

    _field_names = [
        "score_type", "subject", "grade_range",
        "edition", "year", "version", "season",
        "duplicated"
    ]

    def __init__(self,
                 score_type: str,
                 subject: str,
                 grade_range: str,
                 edition: str,
                 year: int,
                 version: str,
                 season: str,
                 duplicated: bool = False,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._score_type = score_type
        self._subject = subject
        self._grade_range = grade_range
        self._edition = edition
        self._year = year
        self._version = version
        self._season = season
        self._duplicated = duplicated

    @property
    def score_type(self) -> str:
        return self._score_type

    @property
    def subject(self) -> str:
        return self._subject

    @property
    def grade_range(self) -> str:
        return self._grade_range

    @property
    def edition(self) -> str:
        return self._edition

    @property
    def year(self) -> int:
        return self._year

    @property
    def version(self) -> str:
        return self._version

    @property
    def season(self) -> str:
        return self._season

    @property
    def duplicated(self) -> bool:
        return self._duplicated


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
    score_type=Converter.for_built_in(str),
    subject=Converter.for_built_in(str),
    grade_range=Converter.for_built_in(str),
    edition=Converter.for_built_in(str),
    year=Converter.for_built_in(int),
    version=Converter.for_built_in(str),
    season=Converter.for_built_in(str),
    duplicated=Converter.for_built_in(bool),
    unit=Converter.for_built_in(str),
)
