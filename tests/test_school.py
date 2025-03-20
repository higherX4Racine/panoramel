#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import astuple

from panoramel import SchoolContext


def test_school_context(mock_uuid):
    context = SchoolContext("Wayside School", "Wayz")

    assert context.context_id == b"1"
    assert astuple(context) == (b"1", "Wayside School", "Wayz")
    assert context.output_name == "School"
    assert context.output_type == str
