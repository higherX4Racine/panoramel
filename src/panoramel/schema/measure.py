# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from ..utilities import unique_integer_id


@dataclass
class Measure[T]:
    column_id: int
    row: int
    value: T
    measure_id: int = unique_integer_id()

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
    def type(self) -> type:
        return type(self.value)
