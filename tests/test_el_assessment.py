#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from polars import String, Float64
from panoramel.el_assessment import ElAssessment


@pytest.mark.parametrize("unit,datatype", [
    ("Status", String),
    ("Value", Float64)
])
def test_el_assessment_context(unit, datatype):
    context = ElAssessment(b"1",
                           "some reading test",
                           "Marzo",
                           1999,
                           unit=unit,
                           )

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1",
                                  "some reading test",
                                  "Marzo",
                                  1999,
                                  unit,
                                  )
    assert context.output_name == unit
    assert context.output_type == datatype
