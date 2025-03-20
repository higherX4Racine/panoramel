#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from smelt_py.database.models.contexts import LookupContext


@dataclass
class StatusValueUnit(LookupContext):
    _name_field = "unit"
    _mapping = {
        "Most Recent Result": float,
        "Status": str,
        "Value": float
    }