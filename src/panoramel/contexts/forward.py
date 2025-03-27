#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema, String, Binary
from smelt_py.matching import (Element, Pattern)
from .status_value_unit_lookup import StatusValueUnit
from .utilities import schema_to_type_map


class Forward(StatusValueUnit):
    r"""One specific early literacy assessment

    Parameters
    ----------
    subject: str
        The subject assessed by this part of the Forward exam
    """
    _field_names = ["subject"]

    def __init__(self, subject: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._subject = subject

    @property
    def subject(self) -> str:
        return self._subject


PATTERN = Pattern(
    [
        Element(pattern=r"Forward"),
        Element(pattern=r"-"),
        Element(name="subject", pattern=r"ELA|Math\\w*"),
        Element(name="unit", pattern=r"Most Recent Result|Status")
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    subject=String,
    unit=String,
))

TYPE_MAP = schema_to_type_map(SCHEMA)
