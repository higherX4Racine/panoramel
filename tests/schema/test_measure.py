# Copyright (C) 2025 by Higher Expectations for Racine County

from math import sqrt

import pytest

from panoramel.schema.measure import Measure


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


@pytest.mark.parametrize("actual_type,lo,hi", [
    (bool, False, True),
    (int, -1, 42),
    (float, 2.71828, 3.14159),
    (str, "a", "z"),
    (CustomObject, CustomObject(0, 1), CustomObject(-1, -1))
])
def test_measure(mock_uuid, actual_type, lo, hi):
    m_lo = Measure(42, 0, lo)
    assert m_lo.measure_id == 1
    assert m_lo.type == actual_type
    m_hi = Measure(42, 1, hi)
    assert m_hi.measure_id == 2
    assert m_hi.type == actual_type

    assert m_lo == m_lo
    assert m_hi == m_hi
    assert m_lo <= m_hi
    assert m_hi >= m_lo

    assert m_lo != m_hi