#  Copyright (C) 2025 by Higher Expectations for Racine County
from dataclasses import dataclass

from polars import Schema, String
from smelt_py.parsing import Element
from smelt_py.models import LookupOutput

from .context import PanoramelContext


@dataclass
class Ela(LookupOutput, PanoramelContext):
    r"""A context that describes either a raw score or a success level.

    Parameters
    ----------
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    """
    _name_field = "unit"
    _mapping = {
        "Status": String,
        "Value": String
    }
    unit: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(pattern=r"^ELA"),
            Element(name="unit", pattern=r"Status|Value", )
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            unit=String
        )
