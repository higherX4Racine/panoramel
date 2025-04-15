#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String, Binary, Float64
from smelt_py.models import LookupOutput
from smelt_py.parsing import Element
from .context import PanoramelContext


@dataclass
class Forward(LookupOutput, PanoramelContext):
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
        "Status": String
    }
    subject: str = None
    unit: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(pattern=r"Forward"),
            Element(pattern=r"-"),
            Element(name="subject", pattern=r"ELA|Math\\w*"),
            Element(name="unit", pattern=r"Most Recent Result|Status")
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            context_id=Binary,
            subject=String,
            unit=String,
        )
