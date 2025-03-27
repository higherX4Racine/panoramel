#  Copyright (C) 2025 by Higher Expectations for Racine County

from polars import Schema, String, Binary

from smelt_py.database.models.contexts import LiteralContext

from .utilities import schema_to_type_map

class School(LiteralContext):
    r"""A table of information about a school.

    Parameters
    ----------
    full_name: str
        The full name of the school
    nick_name: str
        An abbreviated version of the school's name.
    """
    _field_names = ["full_name", "nick_name"]
    _name_field = "School"
    _data_type = str

    def __init__(self,
                 full_name: str,
                 nick_name: str,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)
        self._full_name = full_name
        self._nick_name = nick_name

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def nick_name(self) -> str:
        return self._nick_name


PATTERN = r"(?P<full_name>(?P<nick_name>[A-Z]+[a-z]*).*)"

SCHEMA = Schema(dict(
    context_id=Binary,
    full_name=String,
    nick_name=String,
))

TYPE_MAP = schema_to_type_map(SCHEMA)