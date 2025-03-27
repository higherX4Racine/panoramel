#  Copyright (C) 2025 by Higher Expectations for Racine County

from datetime import date

from polars import Schema, String, Binary

from smelt_py.database.models.contexts import LookupContext
from smelt_py.matching import (Element, Pattern)

from panoramel.contexts.utilities import schema_to_type_map


class Student(LookupContext):
    r"""Identifying information about students.

    Parameters
    ----------
    field: str
        which piece of information the column holds, e.g. name or gender.
    """

    _field_names = ["field"]
    _name_field = "field"
    _mapping = {
        "Date of Birth": date,
        "Gender": str,
        "Grade Level": str,
        "First Name": str,
        "Last Name": str,
        "Student Number": int
    }

    def __init__(self, field: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._field = field

    @property
    def field(self) -> str:
        return self._field


PATTERN = Pattern(
    [
        Element(required=False, pattern=r"Student"),
        Element(name="field",
                pattern=r"|".join([r"Date of Birth",
                                   r"Gender",
                                   r"Grade Level",
                                   r"First Name",
                                   r"Last Name",
                                   r"Student Number"
                                   ]))
    ],
    separator=r"[\s:]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    field=String
))

TYPE_MAP = schema_to_type_map(SCHEMA)
