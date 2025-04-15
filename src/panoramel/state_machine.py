#  Copyright (C) 2025 by Higher Expectations for Racine County

from dataclasses import dataclass, field, InitVar
from typing import Type
from smelt_py.parsing import Parser
from smelt_py.polars import ContextFramer
from .contexts import PanoramelContext


@dataclass
class StateMachine:
    context_type: InitVar[Type[PanoramelContext]]
    parser: Parser = field(init=False)
    framer: ContextFramer = field(init=False)

    def __post_init__(self, context_type: Type[PanoramelContext]):
        self.parser = self.build_parser(context_type)
        self.framer = self.build_framer(context_type)

    @staticmethod
    def build_parser(context_type: Type[PanoramelContext]) -> Parser:
        return context_type.build_parser(context_type.elements(),
                                         context_type.separator)

    @staticmethod
    def build_framer(context_type: Type[PanoramelContext]) -> ContextFramer:
        return ContextFramer(context_type,
                             context_type.build_schema())

    def __call__(self, text: str) -> PanoramelContext | None:
        captures = self.parser.parse(text)
        if captures is not None:
            return self.framer.find_or_append(captures)
        return None