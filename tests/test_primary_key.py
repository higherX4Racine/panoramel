# Copyright (C) 2025 by Higher Expectations for Racine County

from panoramel.primary_key import create_key


def test_mock_key(mock_uuid):
    assert create_key() == 1
    assert create_key() == 2
