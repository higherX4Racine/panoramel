#  Copyright (C) 2025 by Higher Expectations for Racine County
from polars import Int8

from panoramel.contexts import InterventionCountContext


def test_el_intervention_count_context(mock_uuid):
    context = InterventionCountContext(interventions="Number of Interventions")

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", "Number of Interventions")
    assert context.output_name == "Number of Interventions"
    assert context.output_type == Int8
