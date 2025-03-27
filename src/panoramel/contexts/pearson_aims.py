#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema, String, Binary

from smelt_py.matching import (Element, Pattern)

from .status_value_unit_lookup import StatusValueUnit
from .utilities import schema_to_type_map


class PearsonAims(StatusValueUnit):
    r"""Results from standardized assessments of reading for Act 20

    Parameters
    ----------
    assessment: str
        TBH I forget what this captures. sub-score type?
    grade: str
        something in 4k-12
    season: str
        fall, winter, or spring
    """

    _field_names = ["assessment", "grade", "season"]

    def __init__(self,
                 assessment: str,
                 grade: str,
                 season: str,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self._assessment = assessment
        self._grade = grade
        self._season = season

    @property
    def assessment(self) -> str:
        return self._assessment

    @property
    def grade(self) -> str:
        return self._grade

    @property
    def season(self) -> str:
        return self._season


PATTERN = Pattern(
    [
        Element(pattern="aimswebPlus"),
        Element(name="assessment", pattern=r".+"),
        Element(pattern=r"-"),
        Element(name="grade", pattern=r".+"),
        Element(name="season", pattern=r"Fall|Winter|Spring|Summer"),
        Element(name="unit", pattern=r"Status|Value"),
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    assessment=String,
    grade=String,
    season=String,
    unit=String
))

TYPE_MAP = schema_to_type_map(SCHEMA)
