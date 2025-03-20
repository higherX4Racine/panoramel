#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import astuple
import pytest

from panoramel import NweaMapContext


@pytest.mark.parametrize("unit,datatype", [
    ("Status", str),
    ("Value", float)
])
def test_nwea_map_context(mock_uuid, unit, datatype):
    context = NweaMapContext(
        score_type="Growth",
        subject="One of the 3 'R's",
        grade_range="k-12",
        edition="0th",
        year=1999,
        version="pi",
        season="Beckett",
        unit=unit,
        duplicated="eventually convert to boolean"
    )

    assert context.context_id == b"1"
    assert astuple(context) == (
        b"1",
        "Growth",
        "One of the 3 'R's",
        "k-12",
        "0th",
        1999,
        "pi",
        "Beckett",
        unit,
        "eventually convert to boolean"
    )
    assert context.output_name == unit
    assert context.output_type == datatype
