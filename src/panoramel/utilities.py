# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import field
from uuid import uuid4


def create_key() -> int:
    return uuid4().int


def unique_integer_id():
    return field(default_factory=create_key, init=False, repr=False)
