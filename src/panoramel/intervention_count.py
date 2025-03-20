#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from smelt_py.database.models.contexts import LiteralContext


@dataclass
class InterventionCount(LiteralContext):
    number_of_interventions: int
    _name_field = "Number of Interventions"
    _data_type = int