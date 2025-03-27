#  Copyright (C) 2025 by Higher Expectations for Racine County

from importlib.resources import files
from json import load as json_load

import pytest

from panoramel import SchoolContext

with (files("panoramel").joinpath("data", "schools.json").open()) as fh:
    SCHOOL_TUPLES = json_load(fh)


@pytest.mark.parametrize("school", SCHOOL_TUPLES)
def test_school_context(school):
    context = SchoolContext(*school, context_id=b"1")

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", school[0], school[1])
    assert context.output_name == "School"
    assert context.output_type == str
