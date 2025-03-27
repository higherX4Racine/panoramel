#  Copyright (C) 2025 by Higher Expectations for Racine County
from polars import Schema, String, Int8, Int16, Binary
from smelt_py.matching import (Element, Pattern)
from smelt_py.parsing import Converter, MonthConverter, TypeMap

from .status_value_unit_lookup import StatusValueUnit
from .utilities import schema_to_type_map


class ElAssessment(StatusValueUnit):
    r"""One specific early literacy assessment

    Parameters
    ----------
    assessment: str
        The name of the assessment, like "Nonsense Words" or "ORF."
    month: str
        some sloppy representation of the month, like "01" or "Octo."
    year: int
        the four-digit calendar year that the assessment was done in.
    """
    _field_names = ["assessment", "month", "year"]

    def __init__(self,
                 assessment: str,
                 month: str,
                 year: int,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._assessment = assessment
        self._month = month
        self._year = year

    @property
    def assessment(self) -> str:
        return self._assessment

    @property
    def month(self) -> str:
        return self._month

    @property
    def year(self) -> int:
        return self._year


PATTERN = Pattern(
    [
        Element(name="assessment", pattern=r".+"),
        Element(name="month", pattern=r"\b\w+\b"),
        Element(name="year", pattern=r"\b\d+\b"),
        Element(name="unit", pattern=r"Status|Value")
    ],
    r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    assessment=String,
    month=Int8,
    year=Int16,
    unit=String
))

TYPE_MAP = TypeMap(
    assessment=Converter.for_built_in(str),
    month=MonthConverter("en"),
    year=Converter.for_built_in(int),
    unit=Converter.for_built_in(str),
)
