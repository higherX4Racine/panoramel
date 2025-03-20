#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from smelt_py.database.models.contexts import LiteralContext


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

    full_name: str
    nick_name: str

    _name_field = "School"
    _data_type = str