# Copyright (C) 2025 by Higher Expectations for Racine County

from ..utilities import unique_integer_id
from dataclasses import dataclass, field, MISSING


@dataclass
class School:
    name: str = field(default=MISSING)
    school_id: int = unique_integer_id()
