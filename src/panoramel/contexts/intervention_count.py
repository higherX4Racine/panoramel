#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String, Int8

from smelt_py.models import LiteralOutput
from smelt_py.parsing import Element

from .context import PanoramelContext


@dataclass
class InterventionCount(LiteralOutput, PanoramelContext):
    r"""Almost a do-nothing class because the heading holds all information

    Parameters
    ----------
    interventions: int
        The total number of interventions that a student is or has participated in.
    """
    _name_field = "Number of Interventions"
    _data_type = Int8

    interventions: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(name="interventions", pattern=r"Number of Interventions")
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            interventions=String
        )
