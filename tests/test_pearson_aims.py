#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import astuple
import pytest

from panoramel import PearsonAimsContext


@pytest.mark.parametrize("unit,datatype", [
    ("Status", str),
    ("Value", float)
])
def test_pearson_aims_context(mock_uuid, unit, datatype):
    context = PearsonAimsContext(
        "One of the 3 'R's",
        "k-12",
        "Beckett",
        unit
    )

    assert context.context_id == b"1"
    assert astuple(context) == (
        b"1",
        "One of the 3 'R's",
        "k-12",
        "Beckett",
        unit
    )
    assert context.output_name == unit
    assert context.output_type == datatype
