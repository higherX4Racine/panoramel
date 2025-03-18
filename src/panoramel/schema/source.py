# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from datetime import datetime

from ..utilities import unique_integer_id


@dataclass
class Source:
    description: str
    date: datetime
    school_id: int
    source_id: int = unique_integer_id()
