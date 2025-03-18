# Copyright (C) 2025 by Higher Expectations for Racine County

from .keyed_item import KeyedItem
from dataclasses import dataclass


@dataclass
class School(KeyedItem):
    r"""A table of information about a school.

    Parameters
    ----------
    full_name: str
        The full name of the school
    nick_name: str
        An abbreviated version of the school's name.

    Attributes
    ----------
    school_id: int
        The primary key for this item
    key_name: str
        "school_id"

    See Also
    --------
    KeyedItem
    """
    key_name = "school_id"
    full_name: str
    nick_name: str