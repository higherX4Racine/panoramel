#  Copyright (C) 2025 by Higher Expectations for Racine County

from glob import glob
# from importlib.resources import files
# from json import load as json_load
import os
import re

from polars import (
    col,
    read_csv,
    scan_csv,
    DataFrame,
    selectors as cs,
)
from polars import (
    Binary,
    Datetime,
    Float64,
    Int8,
    Int64,
    Object,
    String,
    UInt32,
    UInt64
)
from polars.exceptions import ComputeError

from panoramel import (
    PANORAMA_CONTEXTS
)
from xlsxwriter import Workbook

from smelt_py.polars import ColumnFramer, ContextFramer, MeasureFramer, ModelFramer

DATA_DIR = os.path.join(os.path.expanduser("~"),
                        "Documents",
                        "Data",
                        )

PANORAMA_DOWNLOAD_DIR = os.path.join(DATA_DIR,
                                     "Downloads",
                                     "Racine Unified",
                                     "Early Literacy Continuous Improvement",
                                     "2024-25",
                                     "Panorama")

INPUT_FILES = glob(os.path.join(PANORAMA_DOWNLOAD_DIR, "*.csv"))
OUTPUT_DIR = os.path.join(DATA_DIR, "Iterations", "Panoramel")

MEASURE_FRAMES = {
    data_type: MeasureFramer(data_type) for data_type in [
        Binary,
        Datetime(),
        Float64,
        Int8,
        Int64,
        String,
        UInt32,
        UInt64,
    ]
}

COLUMN_FRAMER = ColumnFramer()

HEADING_KEYS = (
    {"source"}
    .symmetric_difference(PANORAMA_CONTEXTS.keys())
)

CONTEXT_FRAMERS = {
    k: ContextFramer(context, context.build_schema())
    for k, context in PANORAMA_CONTEXTS.items()
}

CONTEXT_PARSERS = {
    k: context.make_parser() for k, context in PANORAMA_CONTEXTS
}

# with files("panoramel").joinpath("data", "schools.json").open() as fh:
#     for pair in json_load(fh):
#         school_context = PANORAMA_CONTEXTS["school"](*pair)
#         CONTEXT_FRAMES["school"].vstack(
#             DataFrame([school_context.as_tuple()],
#                       schema=CONTEXT_FRAMES["school"].schema,
#                       orient="row"),
#             in_place=True
#         )

for fn in INPUT_FILES:
    CONTEXT_FRAMERS["source"].find_or_append(
        CONTEXT_PARSERS["source"].parse(os.path.basename(fn))
    )
    column_names = scan_csv(fn).collect_schema().names()
    columns = []
    for col_index, col_name in enumerate(column_names):
        for heading_key in HEADING_KEYS:
            heading_captures = CONTEXT_PARSERS[heading_key].parse(col_name)
            if heading_captures is not None:
                column = CONTEXT_FRAMERS[heading_key].find_or_append(heading_captures)
                columns.append(column)

    schema = {c.column_id.hex(): c.measure_type for c in columns}
    del columns
    try:
        local = (read_csv(fn,
                          has_header=False,
                          new_columns=schema.keys(),
                          schema=schema,
                          skip_rows=1,
                          )
                 .with_row_index("row", offset=1))
    except ComputeError as c_e:
        print(fn)
        raise c_e
    for data_type, framer in MEASURE_FRAMES.items():
        framer.frame.vstack(
            local
            .select(cs.by_name("row") | cs.by_dtype(data_type))
            .unpivot(index="row", variable_name="column_id", value_name="value")
            .with_columns(col("column_id").str.decode("hex"))
            .select("column_id", "row", "value"),
            in_place=True
        )


def bowdlerize_key(key: str) -> str:
    intermediary = re.match(r"[\w\s]+", key)
    if intermediary is not None:
        return intermediary[0]
    return key


def save_frame_as_sheet(_wb: Workbook, _label: str, _framer: ModelFramer) -> None:
    (framer
    .sanitize_blobs()
    .drop_nulls(
        "value"
    )
    .write_excel(
        _wb,
        _wb.add_worksheet(_label)
    ))


with Workbook(os.path.join(OUTPUT_DIR, "findings.xlsx")) as wb:
    for label, framer in CONTEXT_FRAMERS.items():
        save_frame_as_sheet(wb, bowdlerize_key(label), framer)
    save_frame_as_sheet(wb, "columns", COLUMN_FRAMER)
    for data_type, data_framer in MEASURE_FRAMES.items():
        if data_framer.frame.height > 0:
            save_frame_as_sheet(wb,
                                f"{bowdlerize_key(repr(data_type))}_measures",
                                data_framer)
