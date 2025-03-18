# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from ..utilities import unique_integer_id


@dataclass
class Column:
    source_id: int
    index: int
    context_type: type
    context_id: int
    measure_type: type
    column_id: int = unique_integer_id()