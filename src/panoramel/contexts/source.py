#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass
from datetime import datetime

from polars import Schema, Datetime, String

from smelt_py.models import LiteralOutput
from smelt_py.parsing import Element, Parser
from smelt_py.parsing.converters import (
    BuiltInConverter,
    DateTimeConverter, Converter,
)

from .context import PanoramelContext


@dataclass
class Source(LiteralOutput, PanoramelContext):
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

    separator = r"[_.]"

    @classmethod
    def elements(cls) -> list[Element]:
        return [
            Element(name="full_name", pattern=r".+"),
            Element(pattern=r"students"),
            Element(pattern=r"ELA"),
            Element(pattern=r"YTD"),
            Element(name="date_stamp", pattern=r"\d+"),
            Element(pattern=r"csv")
        ]

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        return super().build_schema(
            full_name=String,
            date_stamp=Datetime()
        )

    @classmethod
    def type_map(cls) -> dict[str, Converter]:
        return dict(
            full_name=BuiltInConverter(str),
            date_stamp=DateTimeConverter("%Y%m%d%H%M%S")
        )
