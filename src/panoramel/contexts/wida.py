#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Float64, String, Schema
from smelt_py.models import LookupOutput
from smelt_py.parsing import Element

from .context import PanoramelContext


@dataclass
class Wida(LookupOutput, PanoramelContext):
    _name_field = "unit"
    _mapping = {
        "Status": String,
        "Value": Float64
    }
    school_year: str = None
    unit: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(r"WIDA"),
            Element(r"\d+-\d+", name="school_year"),
            Element(r"Status|Value", name="unit")
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            school_year=String,
            unit=String
        )
