#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import astuple
import pytest

from panoramel.schema.contexts import ELAssessmentContext


@pytest.mark.parametrize("unit,datatype", [
    ("Status", str),
    ("Value", float)
])
def test_el_assessment_context(mock_uuid, unit, datatype):
    context = ELAssessmentContext("some reading test",
                                  "Marzo",
                                  1999,
                                  unit)

    assert context.context_id == 1
    assert astuple(context) == ("some reading test",
                                "Marzo",
                                1999,
                                unit)
    assert context.output_type == datatype
