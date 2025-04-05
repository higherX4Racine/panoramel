#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from polars import Schema, String, Binary

from smelt_py.models import LiteralContext

from .utilities import schema_to_type_map


@dataclass
class School(LiteralContext):
    r"""A table of information about a school.

    Parameters
    ----------
    full_name: str
        The full name of the school
    nick_name: str
        An abbreviated version of the school's name.
    """

    _name_field = "School"
    _data_type = String

    full_name: str = None
    nick_name: str = None


PATTERN = r"(?P<full_name>(?P<nick_name>[A-Z]+[a-z]*).*)"

SCHEMA = Schema(dict(
    context_id=Binary,
    full_name=String,
    nick_name=String,
))

TYPE_MAP = schema_to_type_map(SCHEMA)
