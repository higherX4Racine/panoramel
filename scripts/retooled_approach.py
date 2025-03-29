#  Copyright (C) 2025 by Higher Expectations for Racine County

from glob import glob
from importlib.resources import files
from json import load as json_load
import os

import polars
from polars import (
    col,
    lit,
    scan_csv,
    Expr,
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
from panoramel import (
    PANORAMA_CONTEXTS,
    PANORAMA_PATTERNS,
    PANORAMA_SCHEMAS,
    PANORAMA_TYPE_MAPS
)

from smelt_py.database.models import Context, Column
from smelt_py.database.models.base import Base as BaseModel

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


def find_or_append(context_frame: DataFrame,
                   context: Context,
                   fields: list[str] = None) -> DataFrame:
    expr = as_filter_expressions(context, fields)
    row = context_frame.filter(*expr)
    if row.height == 0:
        row = as_row(context, context_frame)
        context_frame.vstack(row, in_place=True)
    return row


def as_filter_expressions(model_item: BaseModel,
                          fields: list[str] = None) -> list[Expr]:
    if fields is None:
        fields = model_item.field_names()[1:]
    fields = [(n, getattr(model_item, n)) for n in fields]
    return [col(n) == lit(v) for n, v in fields]


def as_row(model_item: BaseModel, template_frame: DataFrame) -> DataFrame:
    return DataFrame([model_item.as_tuple()],
                     schema=template_frame.schema,
                     orient="row")


def text_to_context(text: str, context_label: str) -> Context | None:
    captures = PANORAMA_PATTERNS[context_label].extract(text)
    if captures:
        return PANORAMA_CONTEXTS[context_label](
            **PANORAMA_TYPE_MAPS[context_label].typed_captures(captures)
        )
    return None


MEASURE_FRAMES = {
    data_type: DataFrame(schema={
        'column_id': Binary,
        'row': UInt32,
        'value': data_type
    }) for data_type in [
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

COLUMN_FRAME = DataFrame(schema={
    'source_id': Binary,
    'index': Int64,
    'context_type': String,
    'context_id': Binary,
    'measure_type': Object
})

HEADING_KEYS = (
    {"source"}
    .symmetric_difference(PANORAMA_PATTERNS.keys())
)

CONTEXT_FRAMES = {
    k: DataFrame(schema=schema)
    for k, schema in PANORAMA_SCHEMAS.items()
}

with files("panoramel").joinpath("data", "schools.json").open() as fh:
    for pair in json_load(fh):
        school_context = PANORAMA_CONTEXTS["school"](*pair)
        CONTEXT_FRAMES["school"].vstack(
            DataFrame([school_context.as_tuple()],
                      schema=CONTEXT_FRAMES["school"].schema,
                      orient="row"),
            in_place=True
        )

for fn in INPUT_FILES:
    source_context = text_to_context(os.path.basename(fn), "source")
    find_or_append(CONTEXT_FRAMES["source"], source_context)
    school_row = find_or_append(CONTEXT_FRAMES["school"],
                                source_context,
                                ["full_name"])
    column_names = scan_csv(fn).collect_schema().names()
    for col_index, col_name in enumerate(column_names):
        for heading_key in HEADING_KEYS:
            heading_context = text_to_context(col_name, heading_key)
            if heading_context is not None:
                context_row = find_or_append(CONTEXT_FRAMES[heading_key],
                                             heading_context)
                column = Column(source_context.context_id, col_index,
                                heading_key, heading_context.context_id,
                                heading_context.output_type)
                COLUMN_FRAME.vstack(as_row(column, COLUMN_FRAME), in_place=True)

    columns = [
        Column(*r) for
        r in
        COLUMN_FRAME.filter(col("source_id") == source_context.context_id).iter_rows()
    ]
    schema = {c.column_id.hex(): c.measure_type for c in columns}
    local = (polars
             .read_csv(fn,
                       has_header=False,
                       new_columns=schema.keys(),
                       schema=schema,
                       skip_rows=1,
                       )
             .with_row_index("row", offset=1))
    for data_type, data_frame in MEASURE_FRAMES.items():
        data_frame.vstack(
            local
            .select(cs.by_name("row") | cs.by_dtype(data_type))
            .unpivot(index="row", variable_name="column_id", value_name="value")
            .with_columns(col("column_id").str.decode("hex"))
            .select("column_id", "row", "value"),
            in_place=True
        )


def safely_print_binaries(_frame, _path):
    (_frame
    .with_columns(
        col(Binary).bin.encode("hex")
    ).write_csv(
        _path
    ))


for label, frame in CONTEXT_FRAMES.items():
    safely_print_binaries(frame,
                          os.path.join(OUTPUT_DIR, f'{label}.csv'))

safely_print_binaries(COLUMN_FRAME
                      .with_columns(col(Object)
                                    .map_elements(repr, return_dtype=String)),
                      os.path.join(OUTPUT_DIR, 'columns.csv'))

for data_type, data_frame in MEASURE_FRAMES.items():
    if data_frame.height > 0:
        basename = f"Measures of {repr(data_type)}.csv"
        safely_print_binaries(data_frame.drop_nulls("value"),
                              os.path.join(OUTPUT_DIR, basename))
