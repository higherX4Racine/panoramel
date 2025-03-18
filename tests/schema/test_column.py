# Copyright (C) 2025 by Higher Expectations for Racine County

from panoramel.schema.column import Column


def test_column(mock_uuid):
    column = Column(42, 0, int, 99, str)

    assert column.column_id == 1
    assert column.source_id == 42
    assert column.index == 0
    assert column.context_type == int
    assert column.context_id == 99
    assert column.measure_type == str
