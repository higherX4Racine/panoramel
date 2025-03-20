#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from datetime import date

from smelt_py.database.models.contexts import LookupContext


@dataclass
class Student(LookupContext):
    field: str

    _name_field = "field"
    _mapping = {
        "Date of Birth": date,
        "Gender": str,
        "Grade Level": str,
        "First Name": str,
        "Last Name": str,
        "Student Number": int
    }
