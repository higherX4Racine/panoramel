# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from typing import Self
from .keyed_item import KeyedItem


@dataclass
class Measure[T](KeyedItem):
    r"""A single typed observation from a parsed table.

    Parameters
    ----------
    column_id: int
        A foreign key to the `Column` object that describes this object's context
    row: int
        The zero-indexed row number whence this observation came
    value: T
        A scalar observation

    Attributes
    ----------
    measure_id: int
        The primary key of this item
    key_name: str
        "measure_id"

    See Also
    --------
    Column
    KeyedItem
    """
    key_name = "measure_id"
    column_id: int
    row: int
    value: T

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return not self > other

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return not self < other

    @property
    def type(self: Self) -> type:
        return type(self.value)
