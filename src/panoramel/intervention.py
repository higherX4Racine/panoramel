#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, Int8, String

from smelt_py.models import LookupOutput
from smelt_py.parsing import Element

from .context import PanoramelContext


@dataclass
class Intervention(LookupOutput, PanoramelContext):
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

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(pattern=r"Intervention"),
            Element(name="number", pattern=r"\d+"),
            Element(name="detail", pattern=r".+")
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            number=Int8,
            detail=String
        )
