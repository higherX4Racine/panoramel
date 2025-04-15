#  Copyright (C) 2025 by Higher Expectations for Racine County
import os.path
import re

from polars import (
    Binary,
    Datetime,
    Float64,
    Int8,
    Int64,
    String,
    UInt32,
    UInt64,
    col,
    read_csv,
    scan_csv,
    selectors as cs, DataFrame,
)
from polars.datatypes import DataTypeClass
from polars.exceptions import ComputeError
from xlsxwriter import Workbook

from smelt_py.models import Column
from smelt_py.polars import ColumnFramer, MeasureFramer, ModelFramer

from . import StateMachine, PANORAMA_CONTEXTS
from .contexts import SourceContext


class Workflow:

    def __init__(self):
        self._measure_framers = {
            data_type: MeasureFramer(data_type) for data_type in self.measure_types()
        }

        self._column_framer = ColumnFramer()
        self._source_machine = StateMachine(SourceContext)
        self._context_machines = {
            k: StateMachine(PANORAMA_CONTEXTS[k]) for k in (
                {"source"}
                .symmetric_difference(
                    PANORAMA_CONTEXTS.keys()
                )
            )
        }

    def __call__(self, full_path: str):
        self.read_measures(
            full_path,
            self.identify_columns(
                os.path.basename(full_path),
                self.get_column_headings(full_path)
            )
        )

    def identify_columns(self,
                         source_text: str,
                         column_headings: list[str]) -> list[Column]:
        source_context = self._source_machine(source_text)
        columns = []
        for index, heading_string in enumerate(column_headings):
            for key, machine in self._context_machines.items():
                heading_context = machine(heading_string)
                if heading_context:
                    column = self._column_framer.add_column(
                        source_context,
                        index,
                        key,
                        heading_context
                    )
                    columns.append(column)
        return columns

    def read_measures(self, file_name: str, columns: list[Column]):
        schema = {c.primary_key.hex(): c.measure_type for c in columns}
        try:
            local = (
                read_csv(file_name,
                         has_header=False,
                         new_columns=schema.keys(),
                         schema=schema,
                         skip_rows=1,
                         )
                .with_row_index("row", offset=1)
            )
        except ComputeError as c_e:
            print(file_name)
            raise c_e
        for data_type, framer in self._measure_framers.items():
            framer.frame.vstack(self.relevant_columns(data_type, local),
                                in_place=True)

    @staticmethod
    def relevant_columns(data_type: DataTypeClass,
                         local: DataFrame) -> DataFrame:
        return (
            local
            .select(
                cs.by_name("row") | cs.by_dtype(data_type)
            )
            .unpivot(
                index="row",
                variable_name="column_id",
                value_name="value"
            )
            .with_columns(
                col("column_id")
                .str.decode("hex")
            )
            .select(
                "column_id",
                "row",
                "value"
            )
        )

    @staticmethod
    def get_column_headings(full_path: str):
        return scan_csv(full_path).collect_schema().names()

    @staticmethod
    def measure_types() -> list[DataTypeClass]:
        return [
            Binary,
            Datetime(),
            Float64,
            Int8,
            Int64,
            String,
            UInt32,
            UInt64,
        ]

    @staticmethod
    def truncate_key(key: str) -> str:
        intermediary = re.match(r"[\w\s]+", key)
        if intermediary is not None:
            return intermediary[0]
        return key

    @staticmethod
    def save_as_sheet(book: Workbook,
                      sheet_name: str,
                      framer: ModelFramer):
        temp_frame = framer.sanitize_blobs()
        null_columns = [s.name for s in temp_frame if s.has_nulls()]
        if null_columns:
            temp_frame = temp_frame.drop_nulls(cs.by_name(null_columns))
        temp_frame.write_excel(
                book,
                book.add_worksheet(sheet_name)
            )


    @classmethod
    def sheet_name_from_type(cls, data_type: DataTypeClass) -> str:
        return f"{cls.truncate_key(repr(data_type))}_measures"

    def save_as_spreadsheet(self, full_path: str):
        with Workbook(full_path) as wb:
            for label, machine in self._context_machines.items():
                self.save_as_sheet(wb,
                                   self.truncate_key(label),
                                   machine.framer)
            self.save_as_sheet(wb,
                               "columns",
                               self._column_framer)
            for dtype, framer in self._measure_framers.items():
                if framer.frame.height > 0:
                    self.save_as_sheet(wb,
                                       self.sheet_name_from_type(dtype),
                                       framer)
