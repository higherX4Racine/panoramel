#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String

from smelt_py.models import LiteralOutput
from smelt_py.parsing import Element

from .context import PanoramelContext


@dataclass
class School(LiteralOutput, PanoramelContext):
    r"""A table of information about a school.

    Parameters
    ----------
    full_name: str
        The full name of the school
    """

    _name_field = "School"
    _data_type = String

    full_name: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [Element(r".+", "full_name")]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            full_name=String
        )
