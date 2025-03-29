#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from polars import String, Float64

from panoramel import PearsonAimsContext


@pytest.mark.parametrize("unit,datatype", [
    ("Status", String),
    ("Value", Float64)
])
def test_pearson_aims_context(mock_uuid, unit, datatype):
    context = PearsonAimsContext(
        "One of the 3 'R's",
        "k-12",
        "Beckett",
        unit
    )

    assert context.context_id == b"1"
    assert context.as_tuple() == (
        b"1",
        "One of the 3 'R's",
        "k-12",
        "Beckett",
        unit
    )
    assert context.output_name == unit
    assert context.output_type == datatype
