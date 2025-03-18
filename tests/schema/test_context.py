# Copyright (C) 2025 by Higher Expectations for Racine County

from panoramel.schema.context import Context


def test_context(mock_uuid):
    first = Context()
    assert first.context_id == 1
    second = Context()
    assert second.context_id == 2
