#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from .status_value_unit_lookup import StatusValueUnit


@dataclass
class NweaMap(StatusValueUnit):
    score_type: str
    subject: str
    grade_range: str
    edition: str
    year: int
    version: str
    season: str
    unit: str
    duplicated: str
