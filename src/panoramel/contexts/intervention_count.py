#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema, String, Binary, Int8

from smelt_py.database.models.contexts import LiteralContext
from smelt_py.matching import (Element, Pattern)

from panoramel.contexts.utilities import schema_to_type_map


class InterventionCount(LiteralContext):
    r"""Almost a do-nothing class because the heading holds all information

    Parameters
    ----------
    interventions: int
        The total number of interventions that a student is or has participated in.
    """
    _field_names = ["interventions"]
    _name_field = "Number of Interventions"
    _data_type = Int8

    def __init__(self, interventions: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._interventions = interventions

    @property
    def interventions(self) -> int:
        return self._interventions


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
