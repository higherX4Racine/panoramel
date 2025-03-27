#  Copyright (C) 2025 by Higher Expectations for Racine County

from datetime import datetime

from polars import Schema, Datetime, String, Binary

from smelt_py.database.models.contexts import LiteralContext
from smelt_py.matching import Element, Pattern
from smelt_py.parsing import Converter, DateTimeConverter, TypeMap

class Source(LiteralContext):
    _field_names = ["full_name", "date_stamp"]
    _name_field = None
    _data_type = None

    def __init__(self, full_name: str, date_stamp: datetime, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._desc = full_name
        self._date = date_stamp

    @property
    def full_name(self) -> str:
        return self._desc

    @property
    def date_stamp(self) -> datetime:
        return self._date


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
    full_name=Converter.for_built_in(str),
    date_stamp=DateTimeConverter("%Y%m%d%H%M%S")
)
