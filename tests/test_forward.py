#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import astuple
import pytest

from panoramel import ForwardContext


@pytest.mark.parametrize("unit,datatype", [
    ("Most Recent Result", float),
    ("Status", str),
    ("Value", float)
])
def test_forward_context(mock_uuid, unit, datatype):
    context = ForwardContext("some reading test", unit)

    assert context.context_id == b"1"
    assert astuple(context) == (b"1", "some reading test", unit)
    assert context.output_name == unit
    assert context.output_type == datatype
