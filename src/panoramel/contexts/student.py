#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema, String, Binary, Datetime, UInt64

from smelt_py.models import LookupContext
from smelt_py import (Element, Pattern)

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
        "504 Status": String,
        "Date of Birth": Datetime(),
        "ELL Status": String,
        "First Name": String,
        "Fit Status": String,
        "Gender": String,
        "Gifted Talented": String,
        "Grade Level": String,
        "Last Name": String,
        "Race Ethnicity": String,
        "Special ED Status": String,
        "Student Number": UInt64
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
                pattern=r"|".join([r"504 Status",
                                   r"Date of Birth",
                                   r"ELL Status",
                                   r"First Name",
                                   r"Fit Status",
                                   r"Gender",
                                   r"Gifted Talented",
                                   r"Grade Level",
                                   r"Last Name",
                                   r"Race Ethnicity",
                                   r"Special ED Status",
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
