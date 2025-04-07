#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String, Float64

from smelt_py.models import LookupOutput
from smelt_py.parsing import Element

from .context import PanoramelContext


@dataclass
class PearsonAims(LookupOutput, PanoramelContext):
    r"""Results from standardized assessments of reading for Act 20

    Parameters
    ----------
    assessment: str
        TBH I forget what this captures. sub-score type?
    grade: str
        something in 4k-12
    season: str
        fall, winter, or spring
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
    grade: str = None
    season: str = None
    unit: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(pattern="aimswebPlus"),
            Element(name="assessment", pattern=r".+"),
            Element(pattern=r"-"),
            Element(name="grade", pattern=r".+"),
            Element(name="season", pattern=r"Fall|Winter|Spring|Summer"),
            Element(name="unit", pattern=r"Status|Value"),
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            assessment=String,
            grade=String,
            season=String,
            unit=String
        )
