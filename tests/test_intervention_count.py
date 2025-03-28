#  Copyright (C) 2025 by Higher Expectations for Racine County
from polars import Int8

from panoramel import InterventionCountContext


def test_el_intervention_count_context(mock_uuid):
    context = InterventionCountContext(42)

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", 42)
    assert context.output_name == "Number of Interventions"
    assert context.output_type == Int8
