#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from typing import ClassVar

from polars import String, Datetime, UInt64, Schema
from polars.datatypes import DataTypeClass

from smelt_py.models import LookupOutput
from smelt_py.parsing import Element

from .context import PanoramelContext


@dataclass
class Student(LookupOutput, PanoramelContext):
    r"""Identifying information about students.

    Parameters
    ----------
    field: str
        which piece of information the column holds, e.g. name or gender.
    """

    _name_field: ClassVar[str] = "field"
    _mapping: ClassVar[dict[str, DataTypeClass]] = {
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

    field: str = None

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(required=False, pattern=r"Student"),
            Element(name="field",
                    pattern=r"|".join(cls._mapping.keys()))
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            field=String
        )
