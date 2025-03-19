# Copyright (C) 2025 by Higher Expectations for Racine County

from panoramel.schema.models import Context


def test_context(mock_uuid):
    first = Context()
    assert first.context_id == b"1"
    second = Context()
    assert second.context_id == b"2"
