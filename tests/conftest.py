import pytest

from panoramel import utilities


@pytest.fixture(scope="package")
def pk_module():
    return utilities


@pytest.fixture(scope="function")
def mock_uuid(pk_module, monkeypatch):
    class MockUUID:
        count = 0
        @property
        def int(self) -> int:
            MockUUID.count += 1
            return MockUUID.count

    monkeypatch.setattr(pk_module,
                        "uuid4",
                        MockUUID)
