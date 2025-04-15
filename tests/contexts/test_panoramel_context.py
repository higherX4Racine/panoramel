#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest

from polars import Binary, Int16
from panoramel.contexts.context import PanoramelContext


def test_abstractness_of_panoramel_context():
    with pytest.raises(NotImplementedError):
        _ = PanoramelContext.elements()

    with pytest.raises(NotImplementedError):
        _ = PanoramelContext.build_parser(PanoramelContext.elements(),
                                          PanoramelContext.separator)


def test_schema_building():
    minimal_schema = PanoramelContext.build_schema()
    assert minimal_schema.len() == 1
    assert minimal_schema["context_id"] == Binary

    populated_schema = PanoramelContext.build_schema(integer=Int16)
    assert populated_schema.len() == 2
    assert populated_schema["context_id"] == Binary
    assert populated_schema["integer"] == Int16
