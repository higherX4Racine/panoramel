#  Copyright (C) 2025 by Higher Expectations for Racine County

import pytest
from polars import Datetime, String, UInt64

from panoramel import StudentContext


@pytest.mark.parametrize("field,datatype", [
    ("Date of Birth", Datetime()),
    ("Gender", String),
    ("Grade Level", String),
    ("First Name", String),
    ("Last Name", String),
    ("Student Number", UInt64)
])
def test_student_context(mock_uuid, field, datatype):
    context = StudentContext(field)

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", field)
    assert context.output_name == field
    assert context.output_type == datatype
