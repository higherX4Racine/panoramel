# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from uuid import uuid4


@dataclass
class KeyedItem:
    r"""A model class with an integer uuid primary key

    Attributes
    ----------
    key_name: str
        The primary key's name for all instances of this class. Defaults to "pk"
    pk: int
        a 128-bit integer representation of a uuid

    See Also
    --------
    uuid.uuid4: the algorithm for making a primary key

    """
    key_name = "pk"

    def __post_init__(self):
        setattr(self, self.key_name, uuid4().int)
