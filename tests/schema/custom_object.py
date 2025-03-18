# Copyright (C) 2025 by Higher Expectations for Racine County

from math import sqrt


class CustomObject:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
        self._m = sqrt(x * x + y * y)

    @property
    def magnitude(self) -> float:
        return self._m

    def __eq__(self, other):
        return self.magnitude == other.magnitude

    def __lt__(self, other):
        return self.magnitude < other.magnitude

    def __gt__(self, other):
        return self.magnitude > other.magnitude
