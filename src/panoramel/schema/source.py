# Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from datetime import datetime

from .keyed_item import KeyedItem


@dataclass
class Source(KeyedItem):
    r"""A description of a downloaded file or fetched blob with Panorama data

    As of 2025, data must be downloaded from Panorama in one CSV sheet per
    school. Consequently, `school_id` is a mandatory foreign key for each
    `Source`.

    Parameters
    ----------
    description: str
        identifying information about the source, like its file name.
    date: datetime
        a timestamp of when the data were pulled from Panorama
    school_id: int
        foreign key to the school that the source describes

    Attributes
    ----------
    source_id : int
        The primary key for this item.
    key_name: str
        "source_id"
    """
    key_name = "source_id"
    description: str
    date: datetime
    school_id: int
