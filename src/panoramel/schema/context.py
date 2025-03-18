# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from .keyed_item import KeyedItem


@dataclass
class Context(KeyedItem):
    r"""Data extracted from the heading of a column.

    Attributes
    ----------
    context_id: int
        The primary key of this item.

    See Also
    --------
    KeyedItem
    """
    key_name = "context_id"
