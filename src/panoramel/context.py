#  Copyright (C) 2025 by Higher Expectations for Racine County
from typing import ClassVar

from polars import Binary, Schema
from smelt_py.models import Context
from smelt_py.parsing import Element, Parser


class PanoramelContext(Context):
    r"""A subclass of `smelt_py.Context` that declares its elements"""

    separator: ClassVar[str] = r"[\s:]"

    @classmethod
    def elements(cls) -> list[Element]:
        r"""The Element instances of the Pattern of the class's Parser."""
        raise NotImplementedError

    @classmethod
    def make_parser(cls) -> Parser:
        r"""Call Context.build_parser with the class's elements"""
        return super().build_parser(cls.elements(), cls.separator)

    @classmethod
    def build_schema(cls, **kwargs) -> Schema:
        r"""create a schema that starts with 'context_id': Binary"""
        return Schema(dict(context_id=Binary) | kwargs)
