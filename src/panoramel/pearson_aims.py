#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from .status_value_unit_lookup import StatusValueUnit


@dataclass
class PearsonAims(StatusValueUnit):
    assessment: str
    grade: str
    season: str
    unit: str
