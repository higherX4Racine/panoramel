#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from polars import Float64, String

from panoramel.contexts import ForwardContext


@pytest.mark.parametrize("unit,datatype", [
    ("Most Recent Result", Float64),
    ("Status", String),
    ("Value", Float64)
])
def test_forward_context(mock_uuid, unit, datatype):
    context = ForwardContext(subject="some reading test", unit=unit)

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", "some reading test", unit)
    assert context.output_name == unit
    assert context.output_type == datatype
