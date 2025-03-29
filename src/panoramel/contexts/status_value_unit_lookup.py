#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Float64, String
from smelt_py.database.models.contexts import LookupContext


class StatusValueUnit(LookupContext):
    r"""A context that describes either a raw score or a success level.

        Parameters
        ----------
        unit: str
            either "Status" or "Value" for an achievement level or raw score.
        """
    _name_field = "unit"
    _mapping = {
        "Most Recent Result": Float64,
        "Status": String,
        "Value": Float64
    }

    def __init__(self, unit: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._unit = unit

    @classmethod
    def field_names(cls) -> list[str]:
        if cls._name_field not in cls._field_names:
            cls._field_names.append(cls._name_field)
        return super().field_names()

    @property
    def unit(self) -> str:
        return self._unit
