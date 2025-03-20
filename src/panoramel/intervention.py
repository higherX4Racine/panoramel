#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from datetime import date

from smelt_py.database.models.contexts import LookupContext

@dataclass
class Intervention(LookupContext):
    Number: int
    Detail: str

    _name_field = "Detail"

    _mapping = {
        "Status": str,
        "Start Date": date,
        "Type and Strategy": str,
        "Tier": str
    }
