#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from .status_value_unit_lookup import StatusValueUnit


@dataclass
class Forward(StatusValueUnit):
    r"""One specific early literacy assessment

    Parameters
    ----------
    subject: str
        The subject assessed by this part of the Forward exam
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    context_id: int
        The primary key for this item.
    """
    subject: str
    unit: str
