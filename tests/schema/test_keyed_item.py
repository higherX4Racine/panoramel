# Copyright (C) 2025 by Higher Expectations for Racine County

from panoramel.schema.keyed_item import KeyedItem


def test_keyed_item(mock_uuid):
    for i in range(1, 9):
        item = KeyedItem()
        assert item.pk == i
