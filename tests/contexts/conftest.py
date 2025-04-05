#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from smelt_py import models


class MockUUID:

    def __init__(self):
        self.count = 0

    @property
    def int(self) -> int:
        self.count += 1
        return self.count

    @property
    def bytes(self) -> bytes:
        return b"%d" % self.int


@pytest.fixture
def mock_uuid(monkeypatch):
    monkeypatch.setattr(models.context, "uuid4", MockUUID)
