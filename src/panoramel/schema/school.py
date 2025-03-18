# Copyright (C) 2025 by Higher Expectations for Racine County

from ..primary_key import create_key
from dataclasses import dataclass, field, MISSING


@dataclass
class School:
    name: str = field(default=MISSING)
    school_id: int = field(default_factory=create_key, init=False, repr=False)
