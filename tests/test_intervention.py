#  Copyright (C) 2025 by Higher Expectations for Racine County

from datetime import date

import pytest
from polars import String, Datetime

from panoramel import InterventionContext


@pytest.mark.parametrize("detail,datatype", [
    ("Status", String),
    ("Start Date", String),
    ("Type and Strategy", String),
    ("Tier", String)
])
def test_intervention_context(mock_uuid, detail, datatype):
    context = InterventionContext(42, detail)

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", 42, detail)
    assert context.output_type == datatype
