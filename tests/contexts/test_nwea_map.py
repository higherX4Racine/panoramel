#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from polars import String, Float64

from panoramel.contexts import NweaMapContext


@pytest.mark.parametrize("unit,datatype", [
    ("Status", String),
    ("Value", Float64)
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
        duplicated=True
    )

    assert context.context_id == b"1"
    assert context.as_tuple() == (
        b"1",
        "Growth",
        "One of the 3 'R's",
        "k-12",
        "0th",
        1999,
        "pi",
        "Beckett",
        True,
        unit,
    )
    assert context.output_name == unit
    assert context.output_type == datatype
    assert context.duplicated


@pytest.mark.parametrize("heading", [
    "NWEA MAP Growth: Spanish Reading 2-5 CCSS 2012 V2 Spring Status",
])
def test_problematic_nwea_map_headings(heading, mock_uuid):
    parser = NweaMapContext.build_parser(NweaMapContext.elements(),
                                         NweaMapContext.separator)

    typed_captures = parser.parse(heading)

    assert typed_captures == {
        "score_type": "Growth",
        "subject": "Spanish Reading",
        "grade_range": "2-5",
        "edition": "CCSS",
        "year": 2012,
        "version": "V2",
        "season": "Spring",
        "duplicated": False,
        "unit": "Status"
    }

    context = NweaMapContext(**typed_captures)

    assert context.as_tuple() == (b"1",
                                 "Growth",
                                 "Spanish Reading",
                                 "2-5",
                                 "CCSS",
                                 2012,
                                 "V2",
                                 "Spring",
                                 False,
                                 "Status",)

    assert context.output_name == "Status"
    assert context.output_type == String


def test_nwea_map_type_map():
    type_map = NweaMapContext.type_map()
    assert type_map["score_type"].type == str
    assert type_map["subject"].type == str
    assert type_map["grade_range"].type == str
    assert type_map["edition"].type == str
    assert type_map["year"].type == int
    assert type_map["version"].type == str
    assert type_map["season"].type == str
    assert type_map["duplicated"].type == bool
    assert type_map["unit"].type == str
