# Copyright (C) 2025 by Higher Expectations for Racine County

from datetime import datetime

from panoramel.schema.source import Source


def test_source_creation(mock_uuid):
    now = datetime.now()
    source = Source("some file or another", now, 42)
    assert source.description == "some file or another"
    assert source.date == now
    assert source.school_id == 42
    assert source.source_id == 1
