#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from datetime import datetime

from polars import Schema, Datetime, String, Binary

from smelt_py.models import LiteralContext
from smelt_py.parsing import (
    Element,
    Parser,
    Pattern,
    TypeMap,
)
from smelt_py.parsing.converters import (
    BuiltInConverter,
    DateTimeConverter,
)


@dataclass
class Source(LiteralContext):
    r"""A Context subclass for tracking the data source of a column.

    Parameters
    ----------
    full_name : str
        some unique identifier for the source, like its basename if it's a file.
    date_stamp: datetime
        the moment in time when the source was downloaded/created/frozen
    """
    _name_field = None
    _data_type = None

    full_name: str = None
    date_stamp: datetime = None


PATTERN = Pattern(
    [
        Element(name="full_name", pattern=r".+"),
        Element(pattern=r"students"),
        Element(pattern=r"ELA"),
        Element(pattern=r"YTD"),
        Element(name="date_stamp", pattern=r"\d+"),
        Element(pattern=r"csv")
    ],
    separator=r"[_\.]"
)

SCHEMA = Schema(dict(
    context_id=Binary,
    full_name=String,
    date_stamp=Datetime()
))

TYPE_MAP = TypeMap(
    full_name=BuiltInConverter(str),
    date_stamp=DateTimeConverter("%Y%m%d%H%M%S")
)

PARSER = Parser(TYPE_MAP, PATTERN)
