# Copyright (C) 2025 by Higher Expectations for Racine County

import pytest

from panoramel.schema import keyed_item


@pytest.fixture(scope="function")
def mock_uuid(monkeypatch):
    class MockUUID:
        count = 0

        @property
        def int(self) -> int:
            MockUUID.count += 1
            return MockUUID.count

    monkeypatch.setattr(keyed_item,
                        "uuid4",
                        MockUUID)
