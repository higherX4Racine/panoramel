#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import astuple
import pytest

from panoramel import ElaContext


@pytest.mark.parametrize("unit,datatype", [
    ("Status", str),
    ("Value", float)
])
def test_ela_context(mock_uuid, unit, datatype):
    context = ElaContext(unit)

    assert context.context_id == b"1"
    assert astuple(context) == (b'1', unit,)
    assert context.output_name == unit
    assert context.output_type == datatype
