# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass

from .keyed_item import KeyedItem


@dataclass
class Column(KeyedItem):
    r"""One observed column from a Panorama data source

    Parameters
    ----------
    source_id: int
        A foreign key to a table of `Source` objects
    index: int
        Which column in the source, starting from zero, it came from
    context_type: type
        The subclass of `Context` that holds data from this column's heading
    measure_type: type
        The datatype of the items in this column's cells.

    Attributes
    ----------
    column_id: int
        The primary key for this item
    key_name: str
        "column_id"

    See Also
    --------
    Context
    Source
    KeyedItem
    """
    key_name = "column_id"
    source_id: int
    index: int
    context_type: type
    context_id: int
    measure_type: type
