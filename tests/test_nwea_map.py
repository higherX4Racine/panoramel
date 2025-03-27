#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from smelt_py.matching import Capture

from panoramel import NweaMapContext
from panoramel.contexts.nwea_map import PATTERN, TYPE_MAP


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
    captures = PATTERN.extract(heading)

    assert captures == [Capture("score_type", "Growth"),
                        Capture("subject", "Spanish Reading"),
                        Capture("grade_range", "2-5"),
                        Capture("edition", "CCSS"),
                        Capture("year", "2012"),
                        Capture("version", "V2"),
                        Capture("season", "Spring"),
                        Capture("unit", "Status"),
                        Capture("duplicated", "")]

    typed_captures = TYPE_MAP.typed_captures(captures)

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
    assert context.output_type == str


def test_nwea_map_type_map():
    assert TYPE_MAP.type("score_type") == str
    assert TYPE_MAP.type("subject") == str
    assert TYPE_MAP.type("grade_range") == str
    assert TYPE_MAP.type("edition") == str
    assert TYPE_MAP.type("year") == int
    assert TYPE_MAP.type("version") == str
    assert TYPE_MAP.type("season") == str
    assert TYPE_MAP.type("duplicated") == bool
    assert TYPE_MAP.type("unit") == str
