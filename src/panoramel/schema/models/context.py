#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass, field
from ..keys import UniqueKey


@dataclass
class Context:
    r"""Data extracted from the heading of a column.

    Attributes
    ----------
    context_id: bytes
        The primary key of this item.
    """
    context_id: UniqueKey = field(default_factory=UniqueKey.new, kw_only=True)
