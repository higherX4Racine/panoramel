# Copyright (C) 2025 by Higher Expectations for Racine County

from re import escape
import pytest
from panoramel.schema.school import School


def test_blank_school(mock_uuid):
    should_be = escape(r"School.__init__() missing 1 required positional argument: 'name'")
    with pytest.raises(TypeError, match=should_be):
        School()


def test_named_school(mock_uuid):
    school = School("Wayside School")
    assert school.school_id == 1
    assert school.name == "Wayside School"
