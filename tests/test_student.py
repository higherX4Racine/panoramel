#  Copyright (C) 2025 by Higher Expectations for Racine County

from datetime import date
import pytest

from panoramel import StudentContext


@pytest.mark.parametrize("field,datatype", [
    ("Date of Birth", date),
    ("Gender", str),
    ("Grade Level", str),
    ("First Name", str),
    ("Last Name", str),
    ("Student Number", int)
])
def test_student_context(mock_uuid, field, datatype):
    context = StudentContext(field)

    assert context.context_id == b"1"
    assert context.as_tuple() == (b"1", field)
    assert context.output_name == field
    assert context.output_type == datatype
