# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from ..models import Context


@dataclass
class ELAssessment(Context):
    r"""One specific early literacy assessment

    Parameters
    ----------
    assessment: str
        The name of the assessment, like "Nonsense Words" or "ORF."
    month: str
        some sloppy representation of the month, like "01" or "Octo."
    year: int
        the four-digit calendar year that the assessment was done in.
    unit: str
        either "Status" or "Value" for an achievement level or raw score.
    context_id: int
        The primary key for this item.
    """
    assessment: str
    month: str
    year: int
    unit: str

    _mapping = {
        "Status": str,
        "Value": float
    }
    @property
    def output_type(self) -> type:
        return self._mapping[self.unit]

