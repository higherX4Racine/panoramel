#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String, Binary, Int8

from smelt_py.models import LiteralContext
from smelt_py.parsing import (Element, Parser, Pattern)

from panoramel.contexts.utilities import schema_to_type_map


@dataclass
class InterventionCount(LiteralContext):
    r"""Almost a do-nothing class because the heading holds all information

    Parameters
    ----------
    interventions: int
        The total number of interventions that a student is or has participated in.
    """
    _name_field = "Number of Interventions"
    _data_type = Int8

    interventions: int = None


PATTERN = Pattern(
    [
        Element(name="interventions", pattern=r"Number of Interventions")
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    interventions=String
))

TYPE_MAP = schema_to_type_map(SCHEMA)

PARSER = Parser(TYPE_MAP, PATTERN)
