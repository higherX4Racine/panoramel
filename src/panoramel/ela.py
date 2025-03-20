#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from .status_value_unit_lookup import StatusValueUnit


@dataclass
class Ela(StatusValueUnit):
    r"""English Language Arts context
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    context_id: int
        The primary key for this item.
    """
    unit: str
